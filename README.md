# BookStoreAPI

> The FastAPI talks about end to end API Developemnt Cycle, Continious Integration and Deployement with the production grade application. We will be deploying the application to Azure App Service.

## Dev Cycle - Initial Configuration

- Folder Configuration.
- Get Settings from environment variable.
- Start the app

> git branch -- 01-devSetting

Git commands used:

```sh
git branch 01-devSetting
git checkout 01-devSetting

```

From Project Root Directory:

```sh

export ENVIRONMENT=dev
export TESTING=0
export TITLE="Bookstore API Documentation"
export VERSION="1.0.1"
```

```python
uvicorn backend.app.run:app --reload
```

## Dev Cycle - Database Configuration

- Database connection URI setting
- Building the DB utils.
- Registering the Configuration.

> git branch -- 02-devSetting

We are going to use the Postgres Database. The Postgres can be get through the cloud service or by spinning a docker container (I have used Postgres on Azure Cloud Service)

you can copy the connection string from the Azure Database for PostgreSQL flexible server.

```sh
export DATABASE_URI_TEST="postgres://{your_username}:{your_password}@{server_initial}.postgres.database.azure.com/bookstoredb?sslmode=require"
export DATABASE_URI_PROD="postgres://{your_username}:{your_password}@{server_initial}.postgres.database.azure.com/bookstoredb?sslmode=require"
```

### What we have created ?

- **db_objects** : Enables Database Connections.
- **core.py** : Here, we added startup and shutdown event handlers, which get executed before the app starts up or when the app is shutting down, respectively.
- **db.py** : here we write the execute and fetch method based on the one or many row, which we are going to refer in the dbfunctions. We will write the functions once we define the router methods. Since we're not generating the schema, we shouldn't see any tables in the database.
