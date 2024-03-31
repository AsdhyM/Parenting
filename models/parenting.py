from init import db, ma 
from marshmallow import fields, validates
from marshmallow.validate import Length, And, Regexp
from marshmallow.exceptions  import ValidationError


VALID_PARENTING = ('Mother', 'Father', 'Grandmother', 'Grandfather')

class Parenting(db.Model):
    __tablename__ = "parentings"

    # Child table properties
    parenting_id = db.Column(db.Integer, primary_key=True)
    parenting = db.Column(db.String(14))
    # Foregin keys
    parent_id = db.Column(db.Integer, db.ForeignKey('parents.parent_id'), nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey('children.child_id'), nullable=False)
    # Relationship with the school table
    parent = db.relationship('Parent', back_populates='parentings')
    child = db.relationship('Child', back_populates='parentings')



class ParentingSchema(ma.Schema):

    name = fields.String(required=True, validate=And(
        Length(min=5, error="Name must be at least 2 characters long"),
        Regexp('^[a-zA-Z0-9]+$', error="Name can only have alphanumeric characters")
    ))

    parenting = fields.String(validate=VALID_PARENTING)
    
    parent = fields.Nested('ParentSchema', only = ['name'])
    child = fields.Nested('ChildSchema', only = ['name'])

    class Meta:
        fields = ('parenting_id', 'parenting', 'parent', 'child')
        ordered = True


parenting_schema = ParentingSchema()
parentings_schema = ParentingSchema(many=True)