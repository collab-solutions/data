from azure.cosmos import CosmosClient, exceptions
from azure.cosmos.container import ContainerProxy
from azure.cosmos.database import DatabaseProxy
from azure.identity import DefaultAzureCredential

from . import config


class CosmosService:
    _settings: config.Settings
    _client: CosmosClient
    _container_name: str 

    def __init__(self, container_name: str, settings: config.Settings):
        self._settings = settings
        self._container_name = container_name

    def _get_client(self) -> CosmosClient:
        if self._client is None:
            credential = DefaultAzureCredential() if self._settings.use_aad_auth else self._settings.account_key
            self._client = CosmosClient(url=self._settings.account_uri, credential=credential)

        return self._client
      
    def _get_container(self) -> ContainerProxy:
        client: CosmosClient = self._get_client()
        database: DatabaseProxy = client.get_database_client(self._settings.database_name)
        return database.get_container_client(self._container_name)
  

class ProductService(CosmosService):
    CONTAINER_NAME = "Products"
    PARTITION_KEY_NAME = "type"

    def __init__(self, settings: config.Settings):
        super().__init__(container_name=self.CONTAINER_NAME, settings=settings)
        
    def get_product_lines(self):
        self._get_by_type("product_line" )
        
        pass
    
    def get_products_by_line(self, product_line_value: str):
        self._get_by_type(product_line_value)  
        
        pass
        
    def _get_by_type(self, product_type: str):
        query = f"SELECT * FROM {self.CONTAINER_NAME} WHERE {self.PARTITION_KEY_NAME} = @product_type"
        
        parameters=[
            dict(name='@product_type', value=product_type)
        ]
        
        container = self._get_container()
        
        pass
      