from datetime import time

from init import db, ma 

from marshmallow import fields, validates
from marshmallow.validate import Length, And, Regexp
from marshmallow.exceptions  import ValidationError

VALID_DAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday') 


class Activity(db.Model):
    __tablename__ = "activities"

    # Activities table properties
    activity_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100)) 
    day = db.Column(db.String, nullable=False)
    time_start = db.Column(db.Time, nullable=False)
    time_end = db.Column(db.Time, nullable=False)

    # Foreign keys
    child_id = db.Column(db.Integer, db.ForeignKey('children.child_id'), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.school_id'), nullable=False)

    # Relationship with the activities table
    child = db.relationship('Child', back_populates='activities')
    school = db.relationship('School', back_populates='activities', cascade='all, delete')
    comments = db.relationship('Comment', back_populates='activities', cascade='all, delete')

class ActivitySchema(ma.Schema):

    name = fields.String(required=True, validate=And(
        Length(min=2, error="Name must be at least 2 characters long"),
        Regexp('^[a-zA-Z0-9]+$', error="Name can only have alphanumeric characters")
    ))

    day = fields.String(validate=VALID_DAYS)

    children = fields.List(fields.Nested('ChildSchema', only = ['name']))
    schools = fields.List(fields.Nested('SchoolSchema', only = ['name']))
    comments = fields.List(fields.Nested('CommentSchema', only = ['name']))

    class Meta:
        fields = ('activity_id', 'name', 'day', 'time_start', 'time_end', 'children', 'schools', 'comments')
        ordered = True

activity_schema = ActivitySchema()
activities_schema = ActivitySchema(many=True) 
