from init import db, ma 
from marshmallow import fields 

class Parent(db.Model):
    __tablename__ = "parents"

    parent_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    dob = db.Column(db.Date, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    mobile = db.Column(db.Integer, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    parentings = db.relationship('Parenting', back_populates='parent', cascade='all, delete')


class ParentSchema(ma.Schema):

    parentings = fields.List(fields.Nested('ParentSchema', only = ['name']))

    class Meta:
        fields = ('parent_id', 'name', 'dob', 'email', 'mobile', 'password', 'is_admin', 'parentings')

parent_schema = ParentSchema(exclude=['password'])
parents_schema = ParentSchema(many=True, exclude=['password'])
