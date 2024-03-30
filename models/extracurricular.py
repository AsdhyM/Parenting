from datetime import datetime

from init import db, ma 
from marshmallow import fields 

class Activity(db.Model):
    __tablename__ = 'activities'

    # Activities table properties
    activity_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String) 
    date = db.Column(db.Date, nullable=False)
    time_start = db.Column(db.Date, nullable=False)
    time_end = db.Column(db.Date, nullable=False)

    # Foreign keys
    child_id = db.Column(db.Integer, db.ForeignKey('children.child_id'), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.school_id'), nullable=False)

    # Relationship with the activities table
    children = db.relationship('Child', back_populates='activities')
    school = db.relationship('School', back_populates='activities', cascade='all, delete')

class ActivitySchema(ma.Schema):

    children = fields.List(fields.Nested('ChildSchema', only = ['name']))
    schools = fields.List(fields.Nested('SchoolSchema', only = ['name']))

    class Meta:
        fields = ('activity_id', 'name', 'date', 'time_start', 'time_end', 'children', 'schools')
        ordered = True

activity_schema = ActivitySchema()
activities_schema = ActivitySchema(many=True) 
