from main import db
from enum import Enum


class SimpleToken(db.Model):

    __tablename__ = 'simple_token'
    id = db.Column(db.Integer(), primary_key=True)
    token = db.Column(db.String(36), nullable=False, unique=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('simple_user.id'))
    created = db.Column(db.String(10))