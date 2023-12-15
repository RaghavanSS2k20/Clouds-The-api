from flask import Flask, jsonify, request, Response
from db.Models.User import User
from  db.Models.Cloud import Cloud
from db.Models.Day import Day

from datetime import datetime
# methods = ["POST"]
def TestcreateCloud():
    data = request.get_json()  
  
    try:
        cloud = Cloud(
            cloud = data['cloudContent']
        )
        cloud.save()
        current_date = datetime.utcnow().date()
       # current_date =  datetime(current_date.year, current_date.month, current_date.day)
        print(current_date)
        day = Day.objects(date=current_date).first()

        if day:
            day.clouds.append(cloud)
        else:
            day = Day(clouds=[cloud])
        day.save()
        return jsonify({"cloud":cloud}), 200
    except Exception as e:
        print("Error while creating cloud , ", str(e))
        return jsonify({"error":str(e)}) , 500




def getAllClouds():
    try:
        all_clouds = Cloud.objects().to_json()
        data = {
            "clouds":all_clouds,
        }
        return Response(all_clouds, mimetype="application/json", status=200 )
    except Exception as e:
        return Response(str(e), status=500, mimetype="application/json")
