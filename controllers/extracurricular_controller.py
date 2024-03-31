from flask import Blueprint, request

from init import db

from models.child import Child, children_schema, child_schema
from models.parent import Parent, parents_schema, parent_schema
from models.parenting import Parenting, parentings_schema, parenting_schema
from models.school import School, schools_schema, school_schema
from models.extracurricular import Activity, activities_schema, activity_schema

activities_bp = Blueprint('activities', __name__, url_prefix='/activities')

# http://localhost:8080/activities
@activities_bp.route('/')
def get_all_activities():
    stmt = db.select(Activity)
    activities = db.session.scalars(stmt)
    return activities_schema.dump(activities)

# http://localhost:8080/activities/"id_number"
@activities_bp.route('/<int:activity_id>')
# activity "id_number"
def get_one_activity(activity_id):
    # select * from activities where id="id_number"
    stmt = db.select(Activity).filter_by(activity_id = activity_id)
    activity = db.session.scalar(stmt)
    if activity:
        return activity_schema.dump(activity)
    else:
        return {"error": f"Activity with id {activity_id} not found"}, 404


# http://localhost:8080/activities
@activities_bp.route('/', methods=["POST"])
def create_activity():
    body_data = request.get_json()
    # Create new activity model instance
    activity = Activity(
        name = body_data.get('name'),
        day = body_data.get('day'),
        time_start = body_data.get('time_start'),
        time_end = body_data.get('time_end'),
        child_id = body_data.get('child_id'),
        school_id = body_data.get('school_id')
    )
    # Add to session and commit
    db.session.add(activity)
    db.session.commit()
    # Return new activity created
    return activity_schema.dump(activity), 201