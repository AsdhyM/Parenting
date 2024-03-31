from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db

from models.child import Child, children_schema, child_schema
from models.parent import Parent, parents_schema, parent_schema
from models.parenting import Parenting, parentings_schema, parenting_schema
from models.school import School, schools_schema, school_schema
from models.extracurricular import Activity, activities_schema, activity_schema
from models.comment import Comment, comment_schema 


comments_bp = Blueprint('comments', __name__, url_prefix="/<int:child_id>/comments") 

# http://localhost:8080/children/child_id/comments - GET, POST
@comments_bp.route('/', methods=["POST"])
@jwt_required()
def create_comment(child_id):
    body_data = request.get_json()
    stmt = db.select(Child).filter_by(child_id=child_id)
    child = db.session.scalar(stmt)
    if child:
        comment = Comment(
            message = body_data.get('message'),
            parent_id = get_jwt_identity(),
            child = child 
        )
        db.session.add(comment)
        db.session.commit()
        return comment.dump(comment), 201
    else:
        return {"error": f"Child with id {child_id} does not exist"}, 404


comments_bp = Blueprint('comments', __name__, url_prefix="/<int:activity_id>/comments") 

# http://localhost:8080/activities/activity_id/comments - GET, POST
@comments_bp.route('/', methods=["POST"])
@jwt_required()
def create_comment(activity_id):
    body_data = request.get_json()
    stmt = db.select(Activity).filter_by(activity_id=activity_id)
    activity = db.session.scalar(stmt)
    if activity:
        comment = Comment(
            message = body_data.get('message'),
            parent_id = get_jwt_identity(),
            activity = activity
        )
        db.session.add(comment)
        db.session.commit()
        return comment.dump(comment), 201
    else:
        return {"error": f"Activity with id {activity_id} does not exist"}, 404


comments_bp = Blueprint('comments', __name__, url_prefix="/<int:school_id>/comments") 

# http://localhost:8080/schools/school_id/comments - GET, POST
@comments_bp.route('/', methods=["POST"])
@jwt_required()
def create_comment(school_id):
    body_data = request.get_json()
    stmt = db.select(School).filter_by(school_id=school_id)
    school = db.session.scalar(stmt)
    if school:
        comment = Comment(
            message = body_data.get('message'),
            parent_id = get_jwt_identity(),
            school = school
        )
        db.session.add(comment)
        db.session.commit()
        return comment.dump(comment), 201
    else:
        return {"error": f"School with id {school_id} does not exist"}, 404