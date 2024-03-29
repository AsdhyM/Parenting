from datetime import timedelta

from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError 
from flask_jwt_extended import create_access_token
from psycopg2 import errorcodes 

from init import db, bcrypt 
from models.parent import Parent, parent_schema




auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route("/register", methods=["POST"])  # /auth/register
def auth_register():
    try:
        # Data from body of the request
        body_data = request.get_json()


        # Create parent instance
        parent = Parent(
            name=body_data.get('name'),
            dob=body_data.get('dob'),
            email=body_data.get('email'),
            mobile=body_data.get('mobile')
        )
        # Password from body of the request
        password = body_data.get('password')
        if password:
            parent.password = bcrypt.generate_password_hash(password).decode('utf-8')
        

        # Add and Commit the parent to Database
        db.session.add(parent)
        db.session.commit()

        # Respond to the parent
        return parent_schema.dump(parent), 201
    
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"The {err.orig.diag.column_name} is required"}
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"error": "Email address already in use"}, 409
    

@auth_bp.route("/login", methods=["POST"])  # /auth/login
def auth_login():
    # get the request body
    body_data = request.get_json()
    # Find the parents with the email address
    stmt = db.select(Parent).filter_by(email=body_data.get("email"))
    # Converting to scalar value
    parent = db.session.scalar(stmt)
    # If parent exists and password is correct
    if parent and bcrypt.check_password_hash(parent.password, body_data.get("password")):
        # Create JWT
        token = create_access_token(identity=str(parent.parent_id), expires_delta=timedelta(days=1))
        # Return the token along with the parent information
        return {"email": parent.email, "token": token, "is_admin": parent.is_admin}
    # else
    else:
        # return error
        return {"error": "Invalid email or password"}, 401