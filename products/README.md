# Products

Details about this data source sample

## Tech Stack

* [FastAPI([FastAPI Tutorials](https://fastapi.tiangolo.com/))

## Setup

VS Code

Setup your VS Code environment following the steps at [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python) 

### Install dependencies

```console
pip install -r requirements.txt
```

If you add additional dependencies, update the requirements file using

```console
pip freeze > requirements.txt
```

### Secrets

Create a `.env` file in the root of folder and paste the following keys in the file. You will need to update any missing values with your values

```text
ACCOUNT_URI=
ACCOUNT_KEY=
USE_AAD_AUTH=false
CREATE_IF_NOT_EXISTS=false
TENANT_ID=
CLIENT_ID=
CLIENT_SECRET=
DATABASE_NAME=
```

### Data

The data is expected to be stored in a container called `product_catalog` that has a partition key named `type`. This data is stored in the [data](data) folder in separate files. If you decide to store this in separate containers you will have to update the [services](services.py) file to match.

You will need to load the data located in [data](data) folder to an Azure Cosmos DB instance. There are various ways you can do this. One example is to use the [Data Migration Tool](https://github.com/AzureCosmosDB/data-migration-desktop-tool?tab=readme-ov-file#azure-cosmos-db-desktop-data-migration-tool).

Here is an example `migrationsettings.json` file you could use if using `dmt`.

```json
{
  "Source": "JSON",
  "Sink": "Cosmos-nosql",
  "SourceSettings": {},
  "SinkSettings": {
    "ConnectionString": "<your connection string here>",
    "Database": "sandbox",
    "RecreateContainer": false,
    "IncludeMetadataFields": false,
    "UseSharedThroughput": true,
    "Container": "product_catalog",
    "PartitionKeyPath": "/type"
  },
  "Operations": [
    {
      "SourceSettings": {
        "FilePath": "/<path to your dir here>/data/products.json"
      }
    },
    {
      "SourceSettings": {
        "FilePath": "/<path to your dir here>/data/product_items.json"
      }
    }
  ]
}
```

### Running

Running locally in dev 

```console
fastapi dev main.py
```

## References

* [FastAPI Tutorials](https://fastapi.tiangolo.com/learn/)
* [Quickstart: Azure Cosmos DB for NoSQL library for Python](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-python?pivots=devcontainer-vscode)