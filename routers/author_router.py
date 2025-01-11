from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from config.config_bd import SessionLocal
from schemas.author_schema import AuthorOut, AuthorCreate, AuthorUpdate
from services.author_service import create_author, read_authors, read_author, update_author, delete_author

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Создание автора
@router.post("/authors", response_model=AuthorOut)
async def post_create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    """Создание автора"""
    return await create_author(db, author)

# Получение списка авторов
@router.get("/authors", response_model=List[AuthorOut])
async def get_read_authors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Получение списка авторов"""
    authors = await read_authors(db, skip, limit)
    return authors

# Получение информации об авторе по id
@router.get("/authors/{id}", response_model=AuthorOut)
async def get_read_author(id: int, db: Session = Depends(get_db)):
    """Получение информации об авторе по id"""
    db_author = await read_author(db, id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author

# Обновление информации об авторе
@router.put("/authors/{id}", response_model=AuthorOut)
async def put_update_author(id: int, reader: AuthorUpdate, db: Session = Depends(get_db)):
    """Обновление информации об авторе"""
    return await update_author(db, id, reader)

# Удаление автора
@router.delete("/authors/{id}", response_model=AuthorOut)
async def delete_delete_author(id: int, db: Session = Depends(get_db)):
    """Удаление автора"""
    return await delete_author(db, id)