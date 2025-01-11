from sqlalchemy.orm import Session

from models.book_models import Book
from schemas.book_schema import BookUpdate, BookCreate


# Добавление книги
async def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Получение информации о книге по id
async def read_book(db: Session, id: int):
    return db.query(Book).filter(Book.id == id).first()

# Получение списка книг
async def read_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()

# Обновление информации о книге
async def update_book(db: Session, id: int, book: BookUpdate):
    db_book = db.query(Book).filter(Book.id == id).first()
    for var, value in vars(book).items():
        setattr(db_book, var, value) if value else None
    db.commit()
    db.refresh(db_book)
    return db_book

# Удаление книги
async def delete_book(db: Session, id: int):
    db_book = db.query(Book).filter(Book.id == id).first()
    db.delete(db_book)
    db.commit()
    return db_book