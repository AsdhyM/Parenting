from init import db, ma 

class Parent(db.Model):
    __tablename__ = "parent"

    parent_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    dob = db.Column(db.Date, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    mobile = db.Column(db.Integer, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)


class ParentSchema(ma.Schema):
    class Meta:
        fields = ('parent_id', 'name', 'dob', 'email', 'mobile', 'password', 'is_admin')

parent_schema = ParentSchema(exclude=['password'])
parents_schema = ParentSchema(many=True, exclude=['password'])
