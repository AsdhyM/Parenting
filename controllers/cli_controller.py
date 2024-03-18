from flask import Blueprint
from init import db, bcrypt
from models.parent import Parent 

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
            image=None,
            email="admin@email.com",
            mobile="0404000000",
            password=bcrypt.generate_password_hash('123456').decode('utf-8'),
            is_admin=True
        ),
        Parent(
            name="User 1",
            dob="2024-02-02",
            image=None,
            email="user1@email.com",
            mobile="0404111111",
            password=bcrypt.generate_password_hash('123456').decode('utf-8')
        )
    ]

    db.session.add_all(parents)
    db.session.commit()

    print("Tables seeded")

