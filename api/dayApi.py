from db.Models.Day import Day
from flask import Blueprint, Response, request
from controller.dayController import getAllDays
dayBp = Blueprint('day', __name__)

#GET
@dayBp.route('/', methods=['GET'])
def getAll():
    return getAllDays()