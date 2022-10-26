from flask import Blueprint, jsonify  # jsonify creates an endpoint response object.
from flask_restful import Api, Resource # used for REST API building.
import requests  # used for testing.

quiz_api = Blueprint('quiz_api', __name__,
                   url_prefix='/api/quiz')
api = Api(quiz_api)

url = "https://opentdb.com/api.php?amount=10&category=19&difficulty=medium&type=multiple"
response = requests.request("GET", url,)
quiz_data = response


#querystring = {"type":"html"}

#response = requests.request("GET", url, params=querystring)

#print(response.text)


