from datetime import date 

from flask import Blueprint

from init import db, bcrypt
from models.parent import Parent 
from models.school import School
from models.child import Child 

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_tables():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_tables():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_tables():
    parents = [
        Parent(
            name="admin name",
            dob="2024-01-01",
            email="admin@email.com",
            mobile="0404000000",
            password=bcrypt.generate_password_hash('123456').decode('utf-8'),
            is_admin=True
        ),
        Parent(
            name="User 1",
            dob="2024-02-02",
            email="user1@email.com",
            mobile="0404111111",
            password=bcrypt.generate_password_hash('123456').decode('utf-8')
        )
    ]

    db.session.add_all(parents)

    schools = [
        School(
            name="Gold Coast Primary"
        ),
        School(
            name="Gold Coast College"
        ),
        School(
            name="Gold Coast Chess"
        ),
        School(
            name="Gold Coast Soccer"
        ),
        School(
            name="Gold Coast Swimming"
        ),
        School(
            name="Gold Coast Jiu-Jitsu"
        )
    ]

    db.session.add_all(schools)


    children = [
        Child(
            name="Gabe Piozzi",
            dob="2010-04-04",
            school=schools[1]
        ),
        Child(
            name="Fabe Piozzi",
            dob="2014-05-05",
            school=schools[0]
        )
    ]

    db.session.add_all(children) 

    db.session.commit()

    print("Tables seeded")

