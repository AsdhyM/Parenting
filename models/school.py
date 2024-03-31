from init import db, ma 

from marshmallow import fields, validates
from marshmallow.validate import Length, And, Regexp
from marshmallow.exceptions  import ValidationError

class School(db.Model):
    __tablename__ = "schools"

    school_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    children = db.relationship('Child', back_populates='school', cascade='all, delete')
    activities = db.relationship('Activity', back_populates='school', cascade='all, delete')
    comments = db.relationship('Comment', back_populates='school', cascade='all, delete')

class SchoolSchema(ma.Schema):

    name = fields.String(required=True, validate=And(
        Length(min=2, error="Name must be at least 2 characters long"),
        Regexp('^[a-zA-Z0-9]+$', error="Name can only have alphanumeric characters")
    ))

    children = fields.List(fields.Nested('ChildSchema', only = ['name']))
    class Meta:
        fields = ('school_id', 'name', 'children')
        ordered = True 

school_schema = SchoolSchema()
schools_schema = SchoolSchema(many=True)