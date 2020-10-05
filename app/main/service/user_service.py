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
        return generate_token(new_user)

        # response_object = {
        #     'status': 'success',
        #     'message': 'Successfully registered'
        # }

        # return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def generate_token(user):
    try:
         # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401

def save_changes(data):
    db.session.add(data)
    db.session.commit()
