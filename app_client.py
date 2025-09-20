# python imports
from dotenv import load_dotenv
import os
import json
import requests

# constants
FASTAPI_URL = "http://44.202.67.155:8000"
ROOT_ENDPOINT = "/"

# load .env and required keys
load_dotenv()
FASTAPI_ACCESS_KEY = os.getenv("FASTAPI_ACCESS_KEY")

# calling root endpoint
#json_body = {
#    "fastapi_access_key": FASTAPI_ACCESS_KEY
#}
response = requests.post(
    FASTAPI_URL + ROOT_ENDPOINT
)
#    json = json_body
#)
response = response.json()
print("Root Endpoint: " + response["response"])