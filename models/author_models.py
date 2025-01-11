from sqlalchemy import Column, Integer, Text, String, DateTime

from config.config_bd import Base


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150))
    biography = Column(Text)
    date_of_birth = Column(DateTime)
