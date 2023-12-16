from flask import Blueprint, Response, request
from db.Models.Cloud import Cloud
from db.Models.Day import Day
from db.Models.User import User
from controller.cloud.CloudController import TestcreateCloud, getAllClouds
from flask_jwt_extended import jwt_required
cloudBp = Blueprint('cloud', __name__)
#Get
@cloudBp.route('/', methods=['GET'])
@jwt_required()
def getAll():
    return getAllClouds()


#POST
@cloudBp.route('/',methods=['POST'])
def testAddCloud():
    return TestcreateCloud()



