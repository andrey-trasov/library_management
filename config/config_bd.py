# Настройка базы данных
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
from databases import Database


DATABASE_URL = "postgresql://postgres:12345@localhost/library_management"


# Движок для синхронного использования
engine = create_engine(DATABASE_URL)
metadata = MetaData()


# Движок для асинхронного использования
database = Database(DATABASE_URL)


# Создание базового класса
Base = declarative_base()


# Создание фабрики сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
