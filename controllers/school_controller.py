from flask import Blueprint, request

from init import db

from models.child import Child, children_schema, child_schema
from models.school import School, schools_schema, school_schema
from models.parenting import Parenting, parentings_schema, parenting_schema
from models.parent import Parent, parents_schema, parent_schema
from models.extracurricular import Activity, activities_schema, activity_schema
from controllers.comment_controller import comments_bp


schools_bp = Blueprint('schools', __name__, url_prefix='/schools') 

# http://localhost:8080/schools - GET
@schools_bp.route('/') 
def get_all_schools():
    stmt = db.select(School)
    schools = db.session.scalars(stmt)
    return schools_schema.dump(schools)

# http://localhost:8080/schools/"id_number" - GET
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


# http://localhost:8080/schools - POST
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

# http:/localhost:8080/schools/"School_id to delete" - DELETE
@schools_bp.route('/<int:school_id>', methods=["DELETE"])
def delete_school(school_id):
    # Get the school from the db with id = school_id
    stmt = db.select(School).filter_by(school_id = school_id)
    school = db.session.scalar(stmt)
    # If school exists
    if school:
        # Delete the school from the session and commit
        db.session.delete(school)
        db.session.commit()
        # Return
        return {'message': f"School '{school.name}' deleted successfully"}
    # else
    else:
        # Return error message
        return {'error': f"School with id {school_id} not found"}, 404 
    
# http://localhost:8080/schools/"school_id to be updated" - PUT, PATCH
@schools_bp.route('/<int:school_id>', methods=["PUT", "PATCH"])
def update_school(school_id):
    # Get the data to be updated from the body of the request
    body_data = request.get_json()
    # Get the school from the db whose fields need to be updated
    stmt = db.select(School).filter_by(school_id=school_id)
    school = db.session.scalar(stmt)
    # If school exists
    if school:
        # Update the fields
        school.name = body_data.get('name') or school.name
        # Commit the changes
        db. session.commit()
        # Return the updated school back
        return school_schema.dump(school)
    # else
    else:
        # Return error message
        return {'error': f'School with id {school_id} not found'}, 404