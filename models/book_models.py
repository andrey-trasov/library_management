from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.orm import relationship

from config.config_bd import Base


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(Text)
    date_of_publication = Column(Date)
    author_id = Column(Integer, ForeignKey('author.id'),)
    genre = Column(String)
    number_books = Column(Integer)

    author = relationship("Author")


