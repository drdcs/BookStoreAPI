from fastapi import FastAPI, Body, Header, APIRouter
from fastapi.param_functions import Depends
from app.models.author import AuthorIn, AuthorOut
from starlette.status import HTTP_201_CREATED
from app.db.repositories.authors import AuthorRepository
from app.api.dependencies.database import get_repository
from typing import List



router = APIRouter()


@router.get("/author")
async def get_all_authors(
    author_repo: AuthorRepository = Depends(get_repository(AuthorRepository))) -> List[AuthorOut]:
    all_authors = await author_repo.get_all_authors()
    return all_authors


@router.post("/author", response_model=AuthorOut, name="author:create-author", status_code=HTTP_201_CREATED)
async def create_new_book(
    new_author: AuthorIn  = Body(..., embed=True),
    author_repo: AuthorRepository = Depends(get_repository(AuthorRepository)),
    ) -> AuthorOut:
    created_author = await author_repo.create_author(new_author=new_author)
    return created_author