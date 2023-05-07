from main import db
from enum import Enum

class UserTypes(Enum):
    ADMIN = 1
    USER = 2
    SUPERADMIN = 3


class UserType(db.Model):

    __tablename__ = 'user_type'
    id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.Integer(), nullable=False, unique=True)
    name = db.Column(db.String(20), nullable=False, unique=True)