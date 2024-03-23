from init import db, ma 
from marshmallow import fields

class Child(db.Model):
    __tablename__ = "child"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    dob = db.Column(db.Date, nullable=False)

    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)

    school = db.relationship('School', back_populates='child')


class ChildSchema(ma.Schema):
    school = fields.Nested('SchoolSchema', only = ['name'])
    class Meta:
        fields = ('id', 'name', 'dob', 'school')

child_schema = ChildSchema()
children_schema = ChildSchema(many=True)
