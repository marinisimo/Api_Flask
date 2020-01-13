from werkzeug.security import safe_str_cmp
from models.user import UserModel

#Example of inmemory data base with ciomprehensions and lists
#users = [
#   User(1,'bob','asdf')
#]

#This...
#username_mapping = { 'bob': {
#        'id': 1,
#        'username': 'bob',
#        'password': 'asdf'
#}}

#Turns to this using List comprehension
#username_mapping = {u.username: u for u in users}
#userid_mapping = {u.id: u for u in users}

def authenticate(username,pwd):
    user = UserModel.find_by_username(username)
    if user and  safe_str_cmp(user.pwd,pwd):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
