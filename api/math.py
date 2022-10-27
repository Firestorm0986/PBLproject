from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing

math_api = Blueprint('math_api', __name__,
                   url_prefix='/api/math')

url = "https://opentdb.com/api.php?amount=10&category=19&difficulty=medium&type=multiple"
server = "http://127.0.0.1:5000/"
math_quiz_url = server + "api/math"


response = requests.request("GET", url)
math_data = response

print(math_data.text)
print(math_data.json())
