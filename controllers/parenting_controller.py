from flask import Blueprint 

from init import db


from models.parenting import Parenting, parentings_schema, parenting_schema


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
    return parenting_schema.dump(parenting)  