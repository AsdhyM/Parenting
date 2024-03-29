from flask import Blueprint, request 

from init import db

from models.child import Child, children_schema, child_schema
from models.parent import Parent, parents_schema, parent_schema
from models.parenting import Parenting, parentings_schema, parenting_schema



children_bp = Blueprint('children', __name__, url_prefix='/children') 

# http://localhost:8080/children
@children_bp.route('/') 
def get_all_children():
    stmt = db.select(Child)
    children = db.session.scalars(stmt)
    return children_schema.dump(children) 


# http://localhost:8080/children/"id_number"
@children_bp.route('/<int:child_id>')
# child "id_number"
def get_one_child(child_id): 
    # select * from children where id="id_number"
    stmt = db.select(Child).filter_by(child_id = child_id)
    child = db.session.scalar(stmt) 
    if child:
        return child_schema.dump(child) 
    else:
        return {"error": f"Child with id {child_id} not found"}, 404 


# http://localhost:8080/children
@children_bp.route('/', methods=["POST"])
def create_child():
    body_data = request.get_json()
    # Create new child model instance
    child = Child(
        name = body_data.get('name'),
        dob = body_data.get('dob'),
        school_id = body_data.get('school_id')
    )
    # Add to session and commit
    db.session.add(child)
    db.session.commit()
    # Return new child created
    return child_schema.dump(child), 201 