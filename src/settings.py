from dotenv import load_dotenv
import os

load_dotenv()

# AWS credentials
HOST = os.getenv('ENDPOINT')
ROOT_CA = os.getenv('ROOT_CA')
CERT = os.getenv('CERT')
KEY = os.getenv('KEY')
PORT = os.getenv('PORT')
THING_NAME = os.getenv('THING_NAME')
CLIENT_ID = os.getenv('CLIENT_ID')
TOPIC = os.getenv('TOPIC')
LOCATION_CODE = os.getenv('LOCATION_CODE')
