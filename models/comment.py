from init import db, ma 

from marshmallow import fields 


class Comment(db.Model):
    __tablename__ = 'comments'

    # Comments table properties
    comment_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    
    # Foreign keys
    parent_id = db.Column(db.Integer, db.ForeignKey('parents.parent_id'), nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey('children.child_id'), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.activity_id'), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.school_id'), nullable=False) 

    # Relationship with the other tables
    parent = db.relationship('Parent', back_populates='comments')
    child = db.relationship('Child', back_populates='comments')
    activities = db.relationships('Activity', back_populates='comments')
    school = db.relationship('School', back_populates='comments')


# Comments schema
class CommentSchema(ma.Schema):

    parents = fields.List(fields.Nested('ParentSchema', only = ['name']))
    children = fields.List(fields.Nested('ChildSchema', only = ['name']))
    activities = fields.List(fields.Nested('ActivitySchema', only = ['name']))
    schools = fields.List(fields.Nested('SchoolSchema', only = ['name']))

    class Meta:
        fields = ('comment_id', 'message', 'parents', 'children', 'activities', 'schools') 
        ordered = True

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True) 