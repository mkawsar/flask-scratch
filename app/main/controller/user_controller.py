from flask import request
from flask_restx import Resource

from ..util.dto import UserDo
from ..service.user_service import save_new_user

api = UserDo.api
_user = UserDo.user


@api.route('/')
class UserList(Resource):
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """ Creates a new user """
        data = request.json
        return save_new_user(data)
