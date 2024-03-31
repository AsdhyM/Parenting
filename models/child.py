from datetime import date 

from init import db, ma 
from marshmallow import fields, validates
from marshmallow.validate import Length, And
from marshmallow.exceptions  import ValidationError

class Child(db.Model):
    __tablename__ = "children"

    # Child table properties
    child_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    dob = db.Column(db.Date, nullable=False)
    # Foregin keys
    school_id = db.Column(db.Integer, db.ForeignKey('schools.school_id'), nullable=False)

    # Relationship with the other tables
    school = db.relationship('School', back_populates='children', cascade='all, delete')
    parentings = db.relationship('Parenting', back_populates='child')
    activities = db.relationship('Activity', back_populates='child', cascade='all, delete')
    comments = db.relationship('Comment', back_populates='child', cascade='all, delete')


# Child Schema
class ChildSchema(ma.Schema):

    name = fields.String(required=True, validate=And(
        Length(min=2, error="Name must be at least 2 characters long")
    ))

    schools = fields.List(fields.Nested('SchoolSchema', only = ['name']))
    parentings = fields.List(fields.Nested('ParentingSchema', exclude=['child']))
    activities = fields.List(fields.Nested('ActivitiesSchema', exclude=['child']))
    comments = fields.List(fields.Nested('CommentsSchema', exclude=['child']))

    class Meta:
        fields = ('child_id', 'name', 'dob', 'schools', 'parentings', 'activities', 'comments') 
        ordered = True

child_schema = ChildSchema()
children_schema = ChildSchema(many=True)
