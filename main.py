from flask import Flask, request, render_template, make_response,jsonify
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
from database import *

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/": {"origins": "https://04b7-178-178-92-202.ngrok-free.app"}})
api = Api(app)
@app.route('/main', methods=['GET'])
@cross_origin(origin='https://04b7-178-178-92-202.ngrok-free.app', headers=['Content-Type', 'Authorization'])
def get():
    return get_user_info(), 200

@app.route('/login', methods=['POST'])
@cross_origin(origin='https://04b7-178-178-92-202.ngrok-free.app', headers=['Content-Type', 'Authorization'])
def login():
    print(request.json)
    name = request.json['name']
    password = request.json['password']
    response = jsonify( valedate_user(name,password))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    return response, 200

@app.route('/signup', methods=['POST'])
@cross_origin(origin='https://04b7-178-178-92-202.ngrok-free.app', headers=['Content-Type', 'Authorization'])
def signup():
    print(request.json)
    namea = request.json['name']
    sex = request.json['sex']
    birthday = request.json['birthday']
    password = request.json['password']
    response = jsonify(create_user(namea,sex,birthday,password))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    return response, 200
     


if __name__ == '__main__':
    app.run(debug=True)
