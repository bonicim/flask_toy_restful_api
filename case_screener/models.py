from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, post_load
from datetime import datetime

db = SQLAlchemy()


class Case(db.Model):
    __tablename__ = "cases"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    accident = db.Column(db.String(80), nullable=False)
    cause = db.Column(db.String(80), nullable=False)
    injury = db.Column(db.String(80), nullable=False)
    viable = db.Column(db.Boolean(), default=False)
    rating = db.Column(db.Integer(), default=0)
    date_created = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return (
            f"<CaseName: {self.name}, CaseId: {self.id}, "
            f"CaseViable: {self.viable}, CaseRating: {self.rating}>"
        )


class CaseSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    email = fields.Email()
    phone_number = fields.Str()
    accident = fields.Str()
    cause = fields.Str()
    injury = fields.Str()
    viable = fields.Boolean()
    rating = fields.Integer()
    date_created = fields.DateTime()

    @post_load
    def make_case(self, data, **kwargs):
        return Case(**data)
