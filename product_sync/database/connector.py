from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from config import Config

products_engine = create_engine(Config.PRODUCTS_DATABASE_URI)
products_db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=products_engine))


Base = declarative_base()