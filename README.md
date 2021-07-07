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
export DATABASE_URI_TEST="postgres://{your_username}:{your_password}@{server_initial}.postgres.database.azure.com/bookstoretest?sslmode=require"
export DATABASE_URI_PROD="postgres://{your_username}:{your_password}@{server_initial}.postgres.database.azure.com/bookstoredb?sslmode=require"
```

### What we have created ?

- **db_objects** : Enables Database Connections.
- **core.py** : Here, we added startup and shutdown event handlers, which get executed before the app starts up or when the app is shutting down, respectively.
- **db.py** : here we write the execute and fetch method based on the one or many row, which we are going to refer in the dbfunctions. We will write the functions once we define the router methods. Since we're not generating the schema, we shouldn't see any tables in the database.

## Dev Cycle - Testing Configuration

- Folder Structure.
- Override Settings from environment variable.
- A simple test-case.

> git branch -- 03-devSetting

We have created a new application for testing. Grab a reference to our database when needed. A simple test-case **test_ping.py** to assert the testing environment.

The Folder Structure would look something like this now. On a side note , you can create a pull request to merge to the main branch.

```tree
├── app
│   ├── configs
│   │   ├── __init__.py
│   │   └── config.py
│   ├── models
│   ├── routes
│   ├── run.py
│   └── utils
│       ├── core.py
│       ├── db.py
│       ├── db_functions.py
│       └── db_objects.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── conftest.py
    └── test_ping.py
```

## Dev Cycle - Model Setting

> git branch -- 04-ModelSetting

we have created models, db repositories and api routers.

- Every API endpoint we define is going to need access to our database - making our postgres db the perfect candidate for a dependency.

- **api/dependencies/database.py** - We have two dependencies here: get_database and get_repository. FastAPI dependencies are just functions - or more accurately Callables - which are called as API endpoint path parameters. These dependancies being used in routes.

```python
@router.post("/book", response_model=BookOut, name="book:create-book", status_code=HTTP_201_CREATED)
async def create_new_book(
    new_book: BookIn = Body(..., embed=True),
    book_repo: BookRepository = Depends(get_repository(BookRepository)),
    ) -> BookOut:
    created_book = await book_repo.create_book(new_book=new_book)
    return created_book
```

By simply specifying the BookIn Python type declaration for new_book, FastAPI will:

- Read the body of the request as JSON.
- Convert the corresponding types.
- Validate the data.
- Respond with an error if validation fails, or provide the route with the model instance needed.

The second of the two path parameters - book_repo - is our database interface, and the route's only dependency. We're setting its default to **Depends(get_repository(BookRepository))** so that we have access to it in our route and can create the new book whenever the function is executed.

```python
def get_database(request: Request) -> Database:
    return request.app.state._db
def get_repository(Repo_type: Type[BaseRepository]) -> Callable:
    def get_repo(db: Database = Depends(get_database)) -> Type[BaseRepository]:
        return Repo_type(db)
    return get_repo
```

In the get_repository function, we declare a single Repo_type parameter and return another function called get_repo. The get_repo has its own dependency - db - declared as a single parameter. This is known in FastAPI as a sub-dependency and depends on the get_database function, which grabs a reference to our database connection that we established in our app's startup event handler.

The Request object comes directly from the starlette framework, and FastAPI handles passing that along for us.
