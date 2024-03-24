from init import db, ma 
from marshmallow import fields

class Child(db.Model):
    __tablename__ = "children"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    dob = db.Column(db.Date, nullable=False)

    school_id = db.Column(db.Integer, db.ForeignKey('schools.school_id'), nullable=False)

    school = db.relationship('School', back_populates='children')


class ChildSchema(ma.Schema):
    school = fields.Nested('SchoolSchema', only = ['name'])

    class Meta:
        fields = ('id', 'name', 'dob', 'school')
        ordered = True


child_schema = ChildSchema()
children_schema = ChildSchema(many=True)
