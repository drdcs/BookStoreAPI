from fastapi import FastAPI, Body, Header, APIRouter
from fastapi.param_functions import Depends
from app.models.book import BookIn, BookOut
from starlette.status import HTTP_201_CREATED
from app.db.repositories.books import BookRepository
from app.api.dependencies.database import get_repository
from typing import List

router = APIRouter()


@router.get("/book")
async def get_all_books(
    book_repo: BookRepository = Depends(get_repository(BookRepository))) -> List[BookOut]:
    all_books = await book_repo.get_all_books()
    return all_books



@router.post("/book", response_model=BookOut, name="book:create-book", status_code=HTTP_201_CREATED)
async def create_new_book(
    new_book: BookIn = Body(..., embed=True),
    book_repo: BookRepository = Depends(get_repository(BookRepository)),
    ) -> BookOut:
    created_book = await book_repo.create_book(new_book=new_book)
    return created_book

    
