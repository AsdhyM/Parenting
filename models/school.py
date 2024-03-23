from init import db, ma 
from marshmallow import fields 


class School(db.Model):
    __tablename__ = "school"

    school_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    child = db.relationship('child', back_populates='school', cascade='all, delete')
    

class SchoolSchema(ma.Schema):
    child = fields.List(fields.Nested('ChildSchema', exclude=['school']))
    class Meta:
        fields = ('school_id', 'name', 'child')

school_schema = SchoolSchema 
schools_schema = SchoolSchema(many=True)