from flask import Response, request, abort, jsonify
from db.Models.User import User
from flask_restful import Resource

class UserResource(Resource):
    def get(self,email):
        try:
            user = User.objects.get(email=email)
            return jsonify({"user":user})
        except User.DoesNotExist:
            return {"message":"user not found"}, 404