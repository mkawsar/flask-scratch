import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data.get('email')).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data.get('email'),
            username=data.get('username'),
            password=data.get('password'),
            createdAt=datetime.datetime.utcnow(),
            updatedAt=datetime.datetime.utcnow()
        )

        save_changes(new_user)

        response_object = {
            'status': 'success',
            'message': 'Successfully registered'
        }

        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_user():
    return User.query.all()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
