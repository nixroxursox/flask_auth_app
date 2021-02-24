from flask_login import UserMixin
import sqlalchemy
import flask_sqlalchemy
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy import (
    Table,
    Column,
    Integer,
    BigInteger,
    String,
    MetaData,
    ForeignKey,
    Sequence,
)
import nacl.pwhash
from sqlalchemy.orm import mapper
import datetime


metadata = MetaData()

Users = Table(
    "Users",
    metadata,
    Column("id", BigInteger, Sequence("users_pk_seq"), primary_key=True),
    Column("name", String, unique=True),
    Column("PIN", String, nullable=False),
    Column("password", String, nullable=False),
    Column("pgp_public_key", Text(3000), nullable=True),
    Column("bip32_key", Text, nullable=True),
    Column("bip32_key_index", BigInteger, nullable=True),
    Column("is_vendor", SmallInteger, default=0),
    Column("created", DateTime, nullable=False, default=func.datetime.now()),
    Column("Modified", DateTime, nullable=False, onupdate=func.utc_times()),
)

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


class User(object):
    def __init__(
        self, name, PIN, password, pgp_public_key, is_vendor, bip32_key, bip32_key_index
    ):
        self.name = name
        self.PIN = PIN
        self.password = password
        self.pgp_public_key = pgp_public_key
        self.is_vendor = is_vendor
        self.bip32_key = bip32_key
        self.bip32_key_index = bip32_key_index


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


mapper(User, Users)
mapper(Product, Products)
