import os

from flask import Flask
from marshmallow.exceptions import ValidationError

from init import db, ma, bcrypt, jwt 

def create_app():
    app = Flask(__name__)

    app.json.sort_keys = False

    # Configurations
    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URI")
    app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")

    # Connect libraries with flask app
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    @app.errorhandler(400)
    def bad_request(err):
        return {"error": str(err)}, 400
    
    @app.errorhandler(404)
    def not_found(err):
        return {"error": str(err)}, 404
    
    @app.errorhandler(ValidationError)
    def validation_error(error):
        return {"error": error.messages}, 400

    from controllers.cli_controller import db_commands
    app.register_blueprint(db_commands) 

    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    from controllers.child_controller import children_bp
    app.register_blueprint(children_bp)

    from controllers.school_controller import schools_bp
    app.register_blueprint(schools_bp)

    from controllers.parenting_controller import parentings_bp
    app.register_blueprint(parentings_bp) 

    from controllers.extracurricular_controller import activities_bp
    app.register_blueprint(activities_bp) 

    return app
