from sqlalchemy.orm import Session

from models.author_models import Author
from schemas.author_schema import AuthorCreate, AuthorUpdate



# Создание автора
async def create_author(db: Session, author: AuthorCreate):
    db_author = Author(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

# Получение информации об авторе по id
async def read_author(db: Session, id: int):
    return db.query(Author).filter(Author.id == id).first()

# Получение списка авторов
async def read_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Author).offset(skip).limit(limit).all()

# Обновление информации об авторе
async def update_author(db: Session, id: int, author: AuthorUpdate):
    db_author = db.query(Author).filter(Author.id == id).first()
    for var, value in vars(author).items():
        setattr(db_author, var, value) if value else None
    db.commit()
    db.refresh(db_author)
    return db_author

# Удаление автора
async def delete_author(db: Session, id: int):
    db_author = db.query(Author).filter(Author.id == id).first()
    db.delete(db_author)
    db.commit()
    return db_author
