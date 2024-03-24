from flask import Blueprint 

from init import db
from models.child import Child, children_schema


children_bp = Blueprint('children', __name__, url_prefix='/children') 

@children_bp.route('/') 
def get_all_children():
    stmt = db.select(Child)
    children = db.session.scalars(stmt)
    return children_schema.dump(children) 