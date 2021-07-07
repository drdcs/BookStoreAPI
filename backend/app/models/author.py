from pydantic import BaseModel
from typing import List, Dict


class AuthorIn(BaseModel):
    name: str
    book: str


class AuthorOut(AuthorIn):
    id: int