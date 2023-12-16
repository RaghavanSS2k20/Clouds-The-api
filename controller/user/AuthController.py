from flask import Flask, jsonify, request
from  db.Models.User import User
from db.Models.Cloud import Cloud
from db.Models.Day import Day
from flask_jwt_extended import create_access_token
import datetime

#POST
def userSignUp():
    try:    
        body = request.get_json()
        phoneNumber = body.get('phoneNumber')
        isUserAvailable = User.objects(phoneNumber=phoneNumber)
        
        if(isUserAvailable):
            return {"message":"user already availabe"}, 409
        user = User(**body)
        user.hash_password()
        user.save()
        data = {
            "user":user
        }
        return {'message':"login successful", "data":data},200
    except Exception as e:
        return {'message':'error while creating user', 'error':str(e)}, 500

def userSignIn():
    body = request.get_json()
    user = User.objects.get(phoneNumber=body.get('phoneNumber'))
    print(user.phoneNumber)
    if(user is None):
        return {"message":"user doesnt exist"}, 404
    
    
    isValid = user.check_password(passWord=body.get("passWord"))
    if(user and not isValid):
        return {"message":"password incorrect"}, 401
    
    expires = datetime.timedelta(days=7)
    access_token = create_access_token(identity=str(user.id), expires_delta=expires)
    return {'token':access_token}, 200