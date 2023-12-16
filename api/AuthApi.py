from controller.user.AuthController import userSignUp, userSignIn
from flask import Blueprint

auth = Blueprint('auth', __name__)
@auth.route('/signup', methods=['POST'])
def signUp():
    return userSignUp()

@auth.route('/signin', methods=['POST'])
def signIn():
    return  userSignIn()
