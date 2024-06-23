from typing import Any, Dict, List
from azure.cosmos import CosmosClient, exceptions
from azure.cosmos.container import ContainerProxy
from azure.cosmos.database import DatabaseProxy
from azure.identity import DefaultAzureCredential
from azure.core.paging import ItemPaged

from config import Settings
from models import Product


class CosmosService:
    _settings: Settings
    _client: CosmosClient | None
    _container_name: str
    _partition_key_name: str

    def __init__(self, container_name: str, partition_key_name: str, settings: Settings):
        self._settings = settings
        self._container_name = container_name
        self._partition_key_name = partition_key_name
        self._client = None

    def _get_client(self) -> CosmosClient:
        if self._client is None:
            credential = DefaultAzureCredential(
            ) if self._settings.use_aad_auth else self._settings.account_key
            self._client = CosmosClient(
                url=self._settings.account_uri, credential=credential)

        return self._client

    def _get_container(self) -> ContainerProxy:
        client: CosmosClient = self._get_client()
        database: DatabaseProxy = client.get_database_client(
            self._settings.database_name)
        return database.get_container_client(self._container_name)

    def query_items(self,
                    query: str,
                    parameters: List[Dict[str, object]] | None = None,
                    enable_cross_partition_query: bool | None = None,
                    **kwargs
                    ) -> ItemPaged[Dict[str, Any]]:
        container = self._get_container()
        return container.query_items(
            query,
            parameters=parameters,
            enable_cross_partition_query=enable_cross_partition_query,
            max_item_count=None,
            **kwargs)


class ProductService(CosmosService):
    CONTAINER_NAME = "products"
    PARTITION_KEY_NAME = "type"

    def __init__(self, settings: Settings):
        super().__init__(container_name=self.CONTAINER_NAME,
                         partition_key_name=self.PARTITION_KEY_NAME,
                         settings=settings)

    def get_product_lines(self) -> List[Product]:
        return self._get_by_type("product_line")

    def get_products_by_line(self, product_line_value: str) -> List[Product]:
        return self._get_by_type(product_line_value)

    def _get_by_type(self, product_type: str) -> List[Product]:
        query = f"SELECT * FROM {self.CONTAINER_NAME} c WHERE c.{self.PARTITION_KEY_NAME} = @product_type"

        parameters: List[Dict[str, object]] = [
            dict(name='@product_type', value=product_type)
        ]

        items = self.query_items(query, parameters)

        products = []
        for item in items:
            product = Product(**item)
            products.append(product)

        return products
