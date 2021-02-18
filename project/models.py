xb
from flask_login import UserMixin


"""
class User(UserMixin, db.Model):
    id = db.Column(
        db.Integer, primary_key=True
    )  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
"""

users = Table(
    "users",
    metadata,
    Column("id", Integer, Sequence("user_id_seq"), primary_key=True),
    Column("name", String(255)),
    Column("PIN", String(144)),
    Column("password", String(144)),
    Column("public_key", String(2000)),
    Column("created", DateTime, nullable=False, default=func.now()),
    Column("Modified", DateTime, nullable=False, onupdate=func.utc_timestamp()),
)


class Users(object):
    def __init__(self, name, PIN, password, public_key):
        self.name = name
        self.PIN = PIN
        self.password = password
        self.public_key = public_key
