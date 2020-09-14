from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and user.password == password:   #safe_str_cmp(a,b) from werkzeug.security import safe_str_cmp
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
