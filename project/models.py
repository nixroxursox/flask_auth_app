import sqlalchemy
import flask_sqlalchemy
from sqlalchemy import (
    Table,
    Column,
    Integer,
    BigInteger,
    String,
    MetaData,
    ForeignKey,
    Sequence,
    Numeric,
    SmallInteger,
    DateTime,
    Text,
    create_engine
)
import nacl.pwhash
from sqlalchemy.orm import mapper
import datetime
from datetime import *
from sqlalchemy.ext.declarative import declarative_base


dbstring = "postgresql+psycopg2://postgres:passw0rd@localhost:5432/postgres"
eng = create_engine(dbstring)

Base = declarative_base()
metadata = MetaData()




Products = Table(
    "Products",
    metadata,
    Column("id", BigInteger, Sequence("products_pk_seq"), primary_key=True),
    Column("name", String(255), nullable=True),
    Column("description", Text, nullable=True),
    Column("price", Numeric, nullable=False),
    Column("user_id", String(255), nullable=True),
    Column("tags", Text, nullable=True),
    Column("is_hidden", SmallInteger, nullable=True, default=0),
    Column("code", String, nullable=True),
    # Column("image", Blob, nullable=True),
    Column("category", BigInteger, nullable=True),
)


class User(Base):
    __tablename__ = 'Users'
    id = Column(BigInteger, Sequence('user_id_seq'), primary_key=True)
    name = Column(String, unique=True)
    PIN = Column(String, nullable=False)
    password = Column(String, nullable=False)
    pgp_public_key = Column(Text(3000), nullable=True)
    bip32_key = Column(Text, nullable=True)
    bip32_key_integer = Column(BigInteger, nullable=True)
    is_vendor = Column(SmallInteger, default=0)
    created = Column(DateTime, nullable=False, default=datetime.utcnow())
    modified = Column(DateTime, nullable=False, onupdate=datetime.utcnow())

def __repr__(self):
    return "<User(name='%s', PIN='%s', password='%s', pgp_public_key='%s', is_vendor='%s', bip32_key='%s', bip32_key_index='%s')>" % (
    self.name,
    self.PIN,
    self.password,
    self.pgp_public_key,
    self.is_vendor,
    self.bip32_key,
    self.bip32_key_index
    )


class Product(object):
    def __init__(
        self, name, description, price, user_id, tags, is_hidden, code, category
    ):
        self.name = name
        self.description = description
        self.price = price
        self.user_id = user_id
        self.tags = tags
        self.is_hidden = is_hidden
        self.code = code
        #    self.image = image
        self.category = category


mapper(Product, Products)
