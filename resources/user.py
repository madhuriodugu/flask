from flask_restful import Resource, reqparse
from pyhtonProject4.models import UserModel


class Userregister(Resource):
    parser= reqparse.RequestParser()
    parser.add_argument("username",
                        type=str,
                        required=True,
                        help='this fiels cannot be blank.')
    parser.add_argument("password",
                        type=str,
                        required=True,
                        help='this fiels cannot be blank.')


    def post(self):
        data = Userregister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400


        user = UserModel(*data)
        user.save_to_db()

        return {'message':"user crested successfully"}, 201

