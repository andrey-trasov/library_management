from datetime import date

from pydantic import BaseModel


class BookBase(BaseModel):
    name: str
    description: str
    date_of_publication: date
    author_id: int
    genre: str
    number_books: int


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookOut(BookBase):
    id: int

    class ConfigDict:
        from_attributes = True