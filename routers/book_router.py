from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from config.config_bd import SessionLocal
from schemas.book_schema import BookCreate, BookOut, BookUpdate
from services.book_service import create_book, read_books, read_book, update_book, delete_book

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Добавление книги
@router.post("/books", response_model=BookOut)
async def post_create_book(book: BookCreate, db: Session = Depends(get_db)):
    """Добавление книги"""
    return await create_book(db, book)

# Получение списка книг
@router.get("/books", response_model=List[BookOut])
async def get_read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Получение списка книг"""
    books = await read_books(db, skip, limit)
    return books

# Получение информации о книге по id
@router.get("/books/{id}", response_model=BookOut)
async def get_read_book(id: int, db: Session = Depends(get_db)):
    """Получение информации о книге по id"""
    db_book = await read_book(db, id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# Обновление информации о книге
@router.put("/books/{id}", response_model=BookOut)
async def put_update_book(id: int, book: BookUpdate, db: Session = Depends(get_db)):
    """Обновление информации о книге"""
    return await update_book(db, id, book)

# Удаление книги
@router.delete("/books/{id}", response_model=BookOut)
async def delete_delete_book(id: int, db: Session = Depends(get_db)):
    """Удаление книги"""
    return await delete_book(db, id)