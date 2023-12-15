from flask import Flask, jsonify, request, Response
from flask_mongoengine import MongoEngine


from db.dbinit import db
from db.dbinit import initdb
from db.Models.Cloud import Cloud
from db.Models.User import User
from dotenv import load_dotenv, find_dotenv
from api.cloudApi import cloudBp
# from api.UserApi.routes import init_routes

import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))
app = Flask(__name__)

print("Mongo uri is ",os.getenv("MONGODB_URI") )
app.config['MONGODB_SETTINGS']={
    'host':os.getenv('MONGODB_URI'),
    'db':'clouds',
    'connect':False
}
try:
    initdb(app)
except Exception as e:
    print(" an error is occured ", e)
finally:
    print("Hpooooooooooooooooooooooooooooorrrrrrrrrrrrrrrrrrraaaaaaaaaayyyyyyy")
# def check_mongo_connection():
#     try:
#         return db.connection.is_connected()
#     except Exception as e:
#         print(e)
#         return False

# if check_mongo_connection():
#     print("Connected to MongoDB")
# else:
#     print("Failed to connect to MongoDB. Please check your configuration.")



@app.route('/')
def index():
    return{"status":'active', "message":'welcome to clouds api'}

@app.route("/add-user", methods = ['POST'])
def addTestUser():
    user = User(email="alittlefightiny@testing.com", phoneNumber="1234567890", passWord="11")
   
    user.displayName = "A Dark Knight"

    user.save()
    return jsonify({'message':"he he hoo hoo", "user":user})
 
@app.route('/users', methods=['GET'])
def getUsers():
    users = User.objects().to_json()
    return Response(users,  mimetype="application/json", status=200)

app.register_blueprint(cloudBp, url_prefix='/api/cloud')
app.run()