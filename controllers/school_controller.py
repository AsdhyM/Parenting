from flask import Blueprint 

from init import db
from models.school import School, schools_schema


schools_bp = Blueprint('schools', __name__, url_prefix='/schools') 

@schools_bp.route('/') 
def get_all_schools():
    stmt = db.select(School)
    schools = db.session.scalars(stmt)
    return schools_schema.dump(schools)
