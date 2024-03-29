from flask import Blueprint, request

from init import db

from models.child import Child, children_schema, child_schema
from models.school import School, schools_schema, school_schema
from models.parenting import Parenting, parentings_schema, parenting_schema

schools_bp = Blueprint('schools', __name__, url_prefix='/schools') 

@schools_bp.route('/') 
def get_all_schools():
    stmt = db.select(School)
    schools = db.session.scalars(stmt)
    return schools_schema.dump(schools)

# http://localhost:8080/schools/"id_number"
@schools_bp.route('/<int:school_id>')
# school "id_number"
def get_one_school(school_id): 
    # select * from schools where id="id_number"
    stmt = db.select(School).filter_by(school_id = school_id) 
    school = db.session.scalar(stmt) 
    if school:
        return school_schema.dump(school) 
    else: 
        return {"error": f"School with id {school_id} not found"}, 404


# http://localhost:8080/schools
@schools_bp.route('/', methods=["POST"])
def create_school():
    body_data = request.get_json()
    # Create new school model instance
    school = School(
        name = body_data.get('name')
    )
    # Add to session and commit
    db.session.add(school)
    db.session.commit()
    # Return new school created
    return school_schema.dump(school), 201
