from app.db.repositories.base import BaseRepository
from app.models.author import AuthorOut, AuthorIn
from typing import List

create_authors_query = """INSERT INTO AUTHORS(name, book)
               VALUES (:name, :book)
               RETURNING id, name, book;
               """


get_all_authors_query = """SELECT * FROM AUTHORS;"""


class AuthorRepository(BaseRepository):
    """
    All database actions associated with the Book resource
    """
    async def create_author(self, *, new_author: AuthorIn) -> AuthorOut:
        query_values = new_author.dict()
        authors = await self.db.fetch_one(query=create_authors_query, values=query_values )
        return AuthorOut(**authors)

    
    async def get_all_authors(self) -> List[AuthorOut]:
        authors = await self.db.fetch_all(query=get_all_authors_query)
        return authors