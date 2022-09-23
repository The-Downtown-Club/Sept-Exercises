from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from config import DATABASE_URI


db_engine = create_engine(DATABASE_URI)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=db_engine))


