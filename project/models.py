from flask_login import UserMixin
import sqlalchemy
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import nacl.pwhash
from sqlalchemy.orm import mapper


Users = Table(
    "Users",
    metadata,
    Column("id", BigInteger, Sequence("users_pk_seq"), primary_key=True),
    Column("name", String, unique=True),
    Column("PIN", String, nullable=False),
    Column("pgp_public_key", Text),
    Column("bip32_key_index", BigInteger),
    Column("is_vendor", SmallInteger, default=0),
    Column("bip32_key", Text),
    Column("created", DateTime, nullable=False, default=func.now()),
    Column("Modified", DateTime, nullable=False, onupdate=func.utc_times()),
)

Products = Table(
    "Products",
    metadata,
    Column("id", BigInteger, nullable=False, Sequence("products_pk_seq"), primary_key=True),
    Column("name", String(255), nullable=True),
    Column("description", Text, nullable=True),
    Column("price", Numeric, nullable=False),
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


class Products(object):
    def __init__(
        self, name, description, price, user_id, tags, is_hidden, code, image, category
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
mapper(Products, Products)
