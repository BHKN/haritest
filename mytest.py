from flask import Flask, jsonify, request
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["details"]

mycol = mydb["driverdetails"]
mycol1=mydb["vehicledetails"]

# creating GET and POST methods for driver details

@app.route('/driver', methods=['GET'])
def driver_details():
    mycol = mydb.driverdetails 
    output = []
    content={}
    for q in mycol.find():
        content= {'driverFullName' : q['driverFullName'],'VehicleNumber' : q['VehicleNumber']}
        output.append(content)
    return jsonify({'result' : output})

@app.route('/type', methods=['POST'])
def hello():
    m = mydb.driverdetails 

    driverFullName = request.json['driverFullName']
    VehicleNumber = request.json['VehicleNumber']

    _id = m.insert({'driverFullName' : driverFullName, 'VehicleNumber' : VehicleNumber})
    new = m.find_one({'_id' : _id})

    output = {'driverFullNmae' : new['driverFullName'], 'VehicleNumber' : new['VehicleNumber']}

    return jsonify({'result' : output})

# creating  GET and POST methods for vehcile details

@app.route('/vehicle', methods=['GET'])
def vehicle_details():
    m1 = mydb.vehicledetails 
    output = []
    content={}
    for q1 in m1.find():
        content= {'VehicleNumber' : q1['VehicleNumber'],'VehicleType':q1['VehicleType'],}
        output.append(content)
    return jsonify({'result' : output})


@app.route('/data', methods=['POST'])
def  hello1():
    m1 = mydb.vehicledetails 

    VehicleType = request.json['VehicleType']
    VehicleNumber = request.json['VehicleNumber']

    _id = m1.insert({'VehicleType' : VehicleType, 'VehicleNumber' : VehicleNumber})
    new = m1.find_one({'_id' : _id})

    output = {'VehicleType' : new['VehicleType'], 'VehicleNumber' : new['VehicleNumber']}

    return jsonify({'result' : output})
    
if __name__ == '__main__':
    app.run(debug=True)