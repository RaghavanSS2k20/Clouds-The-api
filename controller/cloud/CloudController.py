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

def getById(id):
    try:
        cloud = Cloud.objects.get(id=id)
        data  ={
            "cloud":cloud
        }
        return jsonify(data), 200
        if not cloud:
            return jsonify({'error':'cloud not found'}), 404
    except Exception as e:
        return jsonify({"message":"Error while", 'error':str(e)}), 500



#DELETE
def deleteById(id):
    try:
        cloud = Cloud.objects.get(id=id)
        cloud.delete()
        return jsonify({"message":"deleted successfully"}),200
    except Cloud.DoesNotExist:
        return jsonify({'error': 'Cloud not found'}), 404
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500