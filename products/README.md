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
AAD_TENANT_ID=
AAD_CLIENT_ID=
AAD_CLIENT_SECRET=
```

### Running

Running locally in dev 

```console
fastapi dev main.py
```

## References

* [FastAPI Tutorials](https://fastapi.tiangolo.com/learn/)
* [Quickstart: Azure Cosmos DB for NoSQL library for Python](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-python?pivots=devcontainer-vscode)