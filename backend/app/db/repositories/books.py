from app.db.repositories.base import BaseRepository
from app.models.book import BookOut, BookIn
from typing import List

create_books_query = """INSERT INTO BOOKS(isbn, name, author, year)
               VALUES (:isbn, :name, :author, :year)
               RETURNING id, isbn, name, author, year;
               """


get_all_books_query = """SELECT * FROM BOOKS;"""

class BookRepository(BaseRepository):
    """
    All database actions associated with the Book resource
    """
    async def create_book(self, *, new_book: BookIn) -> BookOut:
        query_values = new_book.dict()
        books = await self.db.fetch_one(query=create_books_query, values=query_values )
        return BookOut(**books)

    
    async def get_all_books(self) -> List[BookOut]:
        books = await self.db.fetch_all(query=get_all_books_query)
        return books