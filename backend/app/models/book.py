from pydantic import BaseModel, Schema
from .author import AuthorIn, AuthorOut

class BookIn(BaseModel):
    isbn: str
    name: str
    author: str
    year: int = Schema(None, gt=1900, lt=2100)


class BookOut(BookIn):
    id: int