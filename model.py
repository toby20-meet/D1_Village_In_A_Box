from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()

class Article(Base):
	__tablename__ = 'info'
	id = Column(Integer, primary_key=True)
	title = Column(String)
	url = Column(String)
