from .db import db
from sqlalchemy.schema import ForeignKey


class Comment(db.Model):
  __tablename__ = 'comments'

  id = db.Column(db.Integer, primary_key = True)
  comment = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer,ForeignKey('users.id'), nullable=False)
  transactions_id = db.Column(db.Integer, ForeignKey('transactions.id'), nullable=False)
