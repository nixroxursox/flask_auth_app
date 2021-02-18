import sqlalchemy
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import nacl.pwhash
from sqlalchemy.orm import mapper

db_string = "postgresql+pg8000://postgres:passw0rd@localhost:5432/postgres"
db = sqlalchemy.create_engine(db_string)


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "9OLWxND4o83j4K4iuopO"
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql+psycopg2://postgres:passw0rd@localhost:5432/postgres"

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .models import Users


password = b"passw0rd"
pin = b"9493910663"


db = create_engine(db_string)
metadata = MetaData()

print(nacl.pwhash.argon2id.str(password))
print(nacl.pwhash.argon2id.str(pin))

Users = Table(
    "users",
    metadata,
    Column("id", BigInteger, Sequence("user_id_seq"), primary_key=True),
    Column("name", String, unique=True),
    Column("PIN", String, nullable=False),
    Column("pgp_public_key", Text),
    Column("bip32_key_index", BigInteger),
    Column("is_vendor", SmallInteger, default=0),
    Column("bip32_key", Text),
    Column("created", DateTime, nullable=False, default=func.now()),
    Column("Modified", DateTime, nullable=False, onupdate=func.utc_times
Products = Table(
    "Products",
    metadata,
    Column("id", BigInteger, nullable=True, primary_key=True),
    Column("name", String, nullable=True),
    Column("description", Text, nullable=True),
    Column("price", F                                                                                                                                                                                                                                                                                                                                                           vb                                                       loat, nullable=True),
    Column("tags", Text, nullable=True),
    Column("is_hidden", SmallInteger, nullable=True, default=0),
                                                                                   0

    Column("code", String, nullable=True),
    Column("image", Blob, nullable=True),
    Column("category", BigInteger, nullable=True),
)


class User(object):
    def __init__(
        self, name, PIN, password, pgp_public_key, is_vendor, bip32_key, bip32_key_index
    ):
    ][[='[=========================================================                                                                                                                                                                                                                                                                                                                                                                                                                                                            ]']]
        self.PIN = PIN
        self.password = password
        self.pgp_public_key = pgp_public_key
        self.bip32_key = bip32_key
        sis_vendor


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
        self.image = image
        self.category = category


mapper(User, users)
mapper(Products, Products)

metadata.create_all(db)