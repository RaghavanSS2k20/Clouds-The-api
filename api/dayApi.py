from db.Models.Day import Day
from flask import Blueprint, Response, request
from controller.dayController import getAllDays, getDayByDate, getcurrentDay
dayBp = Blueprint('day', __name__)

# api/day/
#GET
@dayBp.route('/', methods=['GET'])
def getAll():
    return getAllDays()
# api/day/date/<dd-mm-yyyy>
@dayBp.route('/date', methods = ['GET'])
def getByDate():
    return getDayByDate()
# api/day/current
@dayBp.route('/current', methods=['GET'])
def getToday():
    return getcurrentDay()

