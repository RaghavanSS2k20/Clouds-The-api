from ...db.Models.User import User

from flask import jsonify, Response, request


# methods = ['GET']
def getAllUsers():
    try:
        users = User.objects().to_json()
        data = {
            "users":users,
        }
        return Response(users, mimetype="application/json", status=200 )
    except Exception as e:
        return Response(str(e), status=500, mimetype="application/json")


def getUserById(id):
    try:
        user = User.objects(id=id).exclude("passWord").to_json()
        if(user is None):
            return Response("user not found", mimetype="application/json", status=401)
        return Response(user, mimetype="application/json", status=200 )
    except Exception as e:
        return Response(str(e), status=500, mimetype="application/json")

def getUserByEmail(email):
    try:
        user = User.objects(email=email).exclude("passWord").to_json()
        if(user is None):
            return Response("user not found", mimetype="application/json", status=401)
        return Response(user, mimetype="application/json", status=200 )
    except Exception as e:
        return Response(str(e), status=500, mimetype="application/json")

def getUserByPhoneNumber(phoneNumber):
    try:
        user = User.objects(phoneNumber=phoneNumber).exclude("passWord")
        if user is None:
            return {"message":"User not found"}, 404
        return {"message":"user found!", "user":user}
    except Exception as e:
        return {"message":"internal server error while fetching user","error":str(e)}
