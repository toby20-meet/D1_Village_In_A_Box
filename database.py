from model import Base, Article

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(title,url):
	article_object = Article(
		title = title,
		url = url
		)
	session.add(article_object)
	session.commit()
	
def query_all_articles():
	articles = session.query(Article).all()
	return articles

def delete_all_articles():
	session.query(Article).delete()
	session.commit()
