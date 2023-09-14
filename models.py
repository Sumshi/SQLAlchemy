#!/usr/bin/python3

# base model
from sqlalchemy.orm import DeclarativeBase,Mapped,Mapped_column,relationship
from sqlalchemy import ForeignKey,Text

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = Mapped_column(primary_key=True)
    username:Mapped[str] = Mapped_column(nullable=False)
    email_address:Mapped[str]

class Comment(Base):
    __tablename__ = 'comments'
    id:Mapped[int] = Mapped_column(primary_key=True)
    user_id:Mapped[int] = Mapped_column(ForeignKey('users.id'),nullable=False)
    text:Mapped[str] = Mapped_column(Text nullable=False)