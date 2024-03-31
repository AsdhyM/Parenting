from datetime import date 

from flask import Blueprint

from init import db, bcrypt
from models.parent import Parent 
from models.school import School
from models.child import Child 
from models.parenting import Parenting 
from models.extracurricular import Activity

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
            name="Asdhy Piozzi",
            dob="1980-12-22",
            email="admin@email.com",
            mobile="0404000000",
            password=bcrypt.generate_password_hash('123456').decode('utf-8'),
            is_admin=True
        ),
        Parent(
            name="Dad Piozzi",
            dob="1975-02-28",
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

    parentings = [
        Parenting(
            parenting='Mother',
            parent=parents[0],
            child=children[0]
        ),
        Parenting(
            parenting='Mother',
            parent=parents[0],
            child=children[1]
        ),
        Parenting(
            parenting='Father',
            parent=parents[1],
            child=children[0]
        ),
        Parenting(
            parenting='Father',
            parent=parents[1],
            child=children[1]
        )
    ]

    db.session.add_all(parentings) 

    activities = [
        Activity(
            name='Chess',
            day="Wednesday",
            time_start="15:00",
            time_end="16:00",
            child=children[0],
            school=schools[2]
        ),
        Activity(
            name='Soccer',
            day=("Tuesday, Thursday"),
            time_start="15:30",
            time_end="17:00",
            child=children[1],
            school=schools[3]
        ), 
        Activity(
            name='Soccer',
            day=("Saturday"),
            time_start="08:00",
            time_end="10:00",
            child=children[1],
            school=schools[3]
        ),
        Activity(
            name='Swimming',
            day=("Monday, Friday"),
            time_start="15:00",
            time_end="16:00",
            child=children[0],
            school=schools[4]
        ),
        Activity(
            name='Swimming',
            day=("Monday, Friday"),
            time_start="15:00",
            time_end="16:00",
            child=children[1],
            school=schools[4]
        ),
        Activity(
            name='Jiu-Jitsu',
            day="Wednesday",
            time_start="17:00",
            time_end="19:00",
            child=children[0],
            school=schools[5]
        ),
        Activity(
            name='Jiu-Jitsu',
            day="Wednesday",
            time_start="17:00",
            time_end="19:00",
            child=children[1],
            school=schools[5]
        )
    ]

    db.session.add_all(activities) 

    db.session.commit()

    print("Tables seeded")

