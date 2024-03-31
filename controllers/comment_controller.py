# from flask import Blueprint, request

# from init import db

# from models.child import Child, children_schema, child_schema
# from models.parent import Parent, parents_schema, parent_schema
# from models.parenting import Parenting, parentings_schema, parenting_schema
# from models.school import School, schools_schema, school_schema
# from models.extracurricular import Activity, activities_schema, activity_schema
# from models.comment import Comment, comments_schema, comment_schema 


# comment_bp = Blueprint('comments', __name__, url_prefix='/comments') 

# # http://localhost:8080/comments
# @comment_bp.route('/')
# def get_all_comments():
#     stmt = db.select(Comment)
#     comments = db.session.scalar(stmt)
#     return comments_schema.dump(comments)

