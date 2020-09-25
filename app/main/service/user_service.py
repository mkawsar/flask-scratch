import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    response_object = {
        'status': 'success',
        'message': 'Successfully registered'
    }

    return response_object, 201
