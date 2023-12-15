from flask import Flask, jsonify, request
from  db.Models.User import User
from db.Models.Cloud import Cloud
from db.Models.Day import Day

#POST
def userSignUp():
    try:    
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        data = {
            "user":user
        }
        return {'message':"login successful", "data":data},200
    except Exception as e:
        return {'message':'error while creating user', 'error':e}, 500

