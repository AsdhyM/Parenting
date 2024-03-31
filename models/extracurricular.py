from datetime import time

from init import db, ma 

from marshmallow import fields, validates
from marshmallow.validate import OneOf

VALID_DAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday') 


class Activity(db.Model):
    __tablename__ = 'activities'

    # Activities table properties
    activity_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String) 
    day = db.Column(db.String, nullable=False)
    time_start = db.Column(db.Time, nullable=False)
    time_end = db.Column(db.Time, nullable=False)

    # Foreign keys
    child_id = db.Column(db.Integer, db.ForeignKey('children.child_id'), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.school_id'), nullable=False)

    # Relationship with the activities table
    child = db.relationship('Child', back_populates='activities')
    school = db.relationship('School', back_populates='activities', cascade='all, delete')
    #comment = db.relationship('Comment', back_populates='activities', cascade='all, delete')

class ActivitySchema(ma.Schema):

    day = fields.String(validate=OneOf(VALID_DAYS))

    children = fields.List(fields.Nested('ChildSchema', only = ['name']))
    schools = fields.List(fields.Nested('SchoolSchema', only = ['name']))

    class Meta:
        fields = ('activity_id', 'name', 'day', 'time_start', 'time_end', 'children', 'schools')
        ordered = True

activity_schema = ActivitySchema()
activities_schema = ActivitySchema(many=True) 
