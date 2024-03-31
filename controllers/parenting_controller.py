from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db


from models.child import Child, children_schema, child_schema
from models.parent import Parent, parents_schema, parent_schema
from models.parenting import Parenting, parentings_schema, parenting_schema
from models.school import School, schools_schema, school_schema
from models.extracurricular import Activity, activities_schema, activity_schema
from controllers.comment_controller import comments_bp


parentings_bp = Blueprint('parentings', __name__, url_prefix='/parentings') 

# http://localhost:8080/parentings
@parentings_bp.route('/') 
def get_all_parentings():
    stmt = db.select(Parenting)
    parentings = db.session.scalars(stmt)
    return parentings_schema.dump(parentings)

# http://localhost:8080/parentings/"id_number"
@parentings_bp.route('/<int:parenting_id>')
# parenging "id_number"
def get_one_parenting(parenting_id): 
    # select * from parentings where id="id_number"
    stmt = db.select(Parenting).filter_by(parenting_id=parenting_id) 
    parenting = db.session.scalar(stmt) 
    if parenting:
        return parenting_schema.dump(parenting)  
    else:
        return {"error": f"Parenting with id {parenting_id} not found"}, 404


# http://localhost:8080/parentings
@parentings_bp.route('/', methods=["POST"])
@jwt_required()
def create_parenting():
    body_data = request.get_json()
    # Create new parenting model instance
    parenting = Parenting(
        parenting = body_data.get('parenting'),
        parent_id = get_jwt_identity(),
        child_id = body_data.get('child_id')
    )
    # Add to session and commit
    db.session.add(parenting)
    db.session.commit()
    # Return new parenting created
    return parenting_schema.dump(parenting), 201

