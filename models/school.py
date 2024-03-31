from init import db, ma 
from marshmallow import fields 


class School(db.Model):
    __tablename__ = "schools"

    school_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    children = db.relationship('Child', back_populates='school', cascade='all, delete')
    activities = db.relationship('Activity', back_populates='school', cascade='all, delete')
    #comments = db.relationship('Comment', back_populates='school', cascade='all, delete')

class SchoolSchema(ma.Schema):

    children = fields.List(fields.Nested('ChildSchema', only = ['name']))
    class Meta:
        fields = ('school_id', 'name', 'children')
        ordered = True 

school_schema = SchoolSchema()
schools_schema = SchoolSchema(many=True)