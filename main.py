from flask import Flask, render_template, make_response
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
from database import get_user_info

app = Flask(__name__)
@app.route('/main', methods=['GET'])
@cross_origin(origin='https://04b7-178-178-92-202.ngrok-free.app', headers=['Content- Type', 'Authorization'])
def get():
    return get_user_info(), 200
     
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/": {"origins": "https://04b7-178-178-92-202.ngrok-free.app"}})
api = Api(app)

if __name__ == '__main__':
    app.run(debug=True)
