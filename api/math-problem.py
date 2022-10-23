from contextlib import nullcontext
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import time

url = "https://random-math-problem.p.rapidapi.com/random-problem"

querystring = {"type":"html"}

headers = {
	"X-RapidAPI-Key": "cd7cc895ddmshf60d83e19ae6edep1e28a3jsn7c5ab84381c7",
	"X-RapidAPI-Host": "random-math-problem.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)