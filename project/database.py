from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dbstring = "postgresql+psycopg2://postgres:passw0rd@localhost:5432/postgres"

engine = create_engine(dbstring, convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from .models import User
    from .models import Product

    Base.metadata.create_all(bind=engine)


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapper
import logging

dbs = "postgresql+psycopg2://postgres:passw0rd@localhost:5432/postgres"

e = create_engine(dbs, echo=True)
s = sessionmaker(bind=e)
m = MetaData()
