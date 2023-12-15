from flask import Flask, jsonify, request, Response
from db.Models.User import User
from db.Models.Cloud import Cloud
from db.Models.Day import Day

#GET
def getAllDays():
    try:
        allDays = Day.objects()
        data = {
            "days":allDays
        }
        return jsonify({"response":data}), 200
    except Exception as e:
        return jsonify({"message":"error occured while getting allDay"}), 500