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
    sex = request.json['sex']
    birthday = request.json['birthday']
    password = request.json['password']
    response = jsonify(create_user(name,sex,birthday,password))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    return response, 200

@app.route('/create_workout', methods=['POST'])
@cross_origin(origin='https://04b7-178-178-92-202.ngrok-free.app', headers=['Content-Type', 'Authorization'])
def add_workout():
    print(request.json)
    user_id = request.json['user_id']
    steps = request.json['steps']
    distance = request.json['distance']
    speed = request.json['speed']
    pace = request.json['pace']
    calories = request.json['calories']
    duration = request.json['duration']
    response = jsonify(create_workout(user_id, steps, distance, speed, pace, calories, duration))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    return response, 200

@app.route('/workouts', methods=['GET'])
@cross_origin(origin='https://04b7-178-178-92-202.ngrok-free.app', headers=['Content-Type', 'Authorization'])
def get_workouts():
    user = request.args.get('id')
    print(user)
    return get_workout_info(user), 200
     


if __name__ == '__main__':
    app.run(debug=True)
