from init import db, ma 

class Parent(db.Model):
    __tablename__ = "parent"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    dob = db.Column(db.Date, nullable=False)
    image = db.Column(db.LargeBinary)
    email = db.Column(db.String, nullable=False, unique=True)
    mobile = db.Column(db.Integer, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)


class ParentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'dob', 'image', \
                  'email', 'mobile', 'password', 'is_admin')

parent_schema = ParentSchema(exclude=['password'])
parents_schema = ParentSchema(many=True, exclude=['password'])
