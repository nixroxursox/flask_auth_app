import datetime
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
    create_engine,
    func,
    LargeBinary,
)

dbs = "postgresql+psycopg2://postgres:passw0rd@localhost:5432/postgres"
from sqlalchemy.orm import mapper

e = create_engine(dbs)
m = MetaData()

Products = Table(
    "Products",
    m,
    Column(
        "id", BigInteger, Sequence("products_pk_seq"), nullable=False, primary_key=True
    ),
    Column("name", String(255), unique=True, nullable=False),
    Column("description", Text, nullable=True),
    Column("price", Numeric, nullable=False),
    Column("user_id", String(255), unique=True, nullable=False),
    Column("tags", Text, nullable=True),
    Column("is_hidden", SmallInteger, nullable=True, default=0),
    Column("code", String, nullable=True),
    Column("images", LargeBinary, nullable=True),
    Column("category", BigInteger, nullable=True),
)


class Product(object):
    def __init__(
        self, name, description, price, user_id, tags, is_hidden, code, images, category
    ):
        self.name = name
        self.description = description
        self.price = price
        self.user_id = user_id
        self.tags = tags
        self.is_hidden = is_hidden
        self.code = code
        self.images = images
        self.category = category


Users = Table(
    "Users",
    m,
    Column("id", BigInteger, Sequence("user_id_seq"), nullable=False, primary_key=True),
    Column(
        "name",
        String(255),
        nullable=False,
        unique=True,
    ),
    Column("PIN", String, nullable=False),
    Column("password", String, nullable=False),
    Column("pgp_public_key", Text, nullable=True),
    Column("bip32_key", Text, nullable=True),
    Column("bip32_key_integer", BigInteger, nullable=True),
    Column("is_vendor", SmallInteger, default=0),
    Column("created", DateTime, nullable=False, default=func.now()),
    Column("modified", DateTime, nullable=False, onupdate=func.now()),
)


class User(object):
    def __init__(
        self, name, PIN, password, pgp_public_key, bip32_key, bip32_key_index, is_vendor
    ):
        self.name = name
        self.PIN = PIN
        self.password = password
        self.pgp_public_key = pgp_public_key
        self.bip32_key = bip32_key
        self.bip32_key_index = bip32_key_index
        self.is_vendor = is_vendor


Admins = Table(
    "Admins",
    m,
    Column(
        "id", BigInteger, Sequence("admins_pk_seq"), nullable=False, primary_key=True
    ),
    Column(
        "name",
        String(255),
        nullable=False,
        unique=True,
    ),
    Column("admin_bip32_extended_public_key", Text, nullable=False),
    Column("admin_bip32_key_index", BigInteger, nullable=False),
    Column("admin_bitcoin_address", Text, nullable=False),
    Column("permissions", SmallInteger, nullable=False),
    Column("isModerator", SmallInteger, nullable=True, default=0),
)


class Admin(object):
    def __init__(
        self,
        name,
        admin_bip32_extended_public_key,
        admin_bip32_key_index,
        admin_bitcoin_address,
        permissions,
        isModerator,
    ):
        self.name = name
        self.admin_bip32_extended_public_key = admin_bip32_extended_public_key
        self.admin_bip32_key_index = admin_bip32_key_index
        self.admin_bitcoin_address = admin_bitcoin_address
        self.permissions = permissions
        sef.isModerator = isModerator


mapper(Product, Products)
mapper(User, Users)
mapper(Admin, Admins)

m.create_all(e)
