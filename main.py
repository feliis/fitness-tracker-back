from flask import Flask, jsonify, make_response, render_template, request
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource

from database import *

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/": {"origins": "https://04b7-178-178-92-202.ngrok-free.app"}})
api = Api(app)


@app.route('/profile', methods=['GET'])
@cross_origin(origin='https://04b7-178-178-92-202.ngrok-free.app', headers=['Content-Type', 'Authorization'])
def get():
    user = request.args.get('id')
    print(user)
    return get_user_info(user), 200

@app.route('/login', methods=['POST'])
@cross_origin(origin='https://04b7-178-178-92-202.ngrok-free.app', headers=['Content-Type', 'Authorization'])
def login():
    print(request.json)
    name = request.json['name']
    password = request.json['password']
    response = jsonify(valedate_user(name,password))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    return response, 200

@app.route('/signup', methods=['POST'])
@cross_origin(origin='https://04b7-178-178-92-202.ngrok-free.app', headers=['Content-Type', 'Authorization'])
def signup():
    print(request.json)
    name = request.json['name']
    lastname = request.json['lastname']
    username = request.json['username']
    sex = request.json['sex']
    birthday = request.json['birthday']
    height = request.json['height']
    weight = request.json['weight']
    password = request.json['password']
    response = jsonify(create_user(name,lastname,username,sex,birthday,height,weight,password))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    return response, 200

@app.route('/create_workout', methods=['POST'])
@cross_origin(origin='https://04b7-178-178-92-202.ngrok-free.app', headers=['Content-Type', 'Authorization'])
def add_workout():
    print(request.json)
    user_id = request.json['user_id']
    type_activity = request.json['type_activity']
    steps = request.json['steps']
    distance = request.json['distance']
    speed = request.json['speed']
    pace = request.json['pace']
    calories = request.json['calories']
    duration = request.json['duration']
    date_start = request.json['date_start']
    date_stop = request.json['date_stop']
    coordinates = request.json['coordinates']
    response = jsonify(create_workout(user_id, type_activity, steps, distance, speed, pace, calories, duration, date_start, date_stop,coordinates))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    return response, 200

@app.route('/workouts', methods=['GET'])
@cross_origin(origin='https://04b7-178-178-92-202.ngrok-free.app', headers=['Content-Type', 'Authorization'])
def workouts():
    user = request.args.get('id')
    return get_workouts(user), 200
     
@app.route('/workout', methods=['GET'])
@cross_origin(origin='https://04b7-178-178-92-202.ngrok-free.app', headers=['Content-Type', 'Authorization'])
def workout_info():
    workout_id = request.args.get('id')
    print(workout_id)
    return get_workout_info(workout_id), 200

@app.route('/activities', methods=['GET'])
@cross_origin(origin='https://04b7-178-178-92-202.ngrok-free.app', headers=['Content-Type', 'Authorization'])
def activities():
    return get_activities(), 200

if __name__ == '__main__':
    app.run(debug=True)
