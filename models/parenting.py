from init import db, ma 
from marshmallow import fields

class Parenting(db.Model):
    __tablename__ = "parentings"

    # Child table properties
    parenting_id = db.Column(db.Integer, primary_key=True)
    parenting = db.Column(db.String)
    # Foregin keys
    parent_id = db.Column(db.Integer, db.ForeignKey('parents.parent_id'), nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey('children.child_id'), nullable=False)
    # Relationship with the school table
    parent = db.relationship('Parent', back_populates='parentings')
    child = db.relationship('Child', back_populates='parentings')



class ParentingSchema(ma.Schema):

    parent = fields.Nested('ParentSchema', only = ['name'])
    children = fields.Nested('ChildSchema', only = ['name'])

    class Meta:
        fields = ('parenting_id', 'parenting', 'parent', 'children')
        ordered = True


parenting_schema = ParentingSchema()
parentings_schema = ParentingSchema(many=True)