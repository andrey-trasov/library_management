from datetime import datetime

from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str
    biography: str
    date_of_birth: datetime

class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorBase):
    pass


class AuthorOut(AuthorBase):
    id: int


    class ConfigDict:
        from_attributes = True
