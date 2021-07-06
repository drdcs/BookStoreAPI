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
