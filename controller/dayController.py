from flask import Flask, jsonify, request, Response
from db.Models.User import User
from db.Models.Cloud import Cloud
from db.Models.Day import Day
from datetime import datetime

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


def getcurrentDay():
    try:
        current_date = datetime.utcnow().date()
        day = Day.objects(date=current_date).first()
        if day:
            return jsonify({"today":day, "message":"day found"}), 200
        else:
            day = Day()
            return jsonify({"message":"Day not found, created","today":day})

    except Exception as e:
        return jsonify({"message":"internal server error while getting today", "error":str(e)})

def getDayByDate():
    try:
        target_date_str = request.args.get('date')
        target_date = datetime.strptime(target_date_str, '%Y-%m-%d').date()
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid date format'}), 400

    day_entry = Day.objects(date=target_date).first()

    if day_entry:
        # You may want to serialize the data before sending it
        data = {
            'clouds': [cloud.to_dict() for cloud in day_entry.clouds],
            'mostNoticedEmotion': day_entry.mostNoticedEmotion,
            'date': day_entry.date.isoformat(),
        }
        return jsonify(data)
    else:
        return jsonify({'error': f'No data found for {target_date}'}), 404