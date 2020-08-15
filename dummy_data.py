from datetime import datetime
import json
import random

from .settings import LOCATION_CODE

def generate_random_data():
    ts = datetime.timestamp(datetime.now())
    direction = random.randrange(1, 360)
    humidity = random.randrange(90, 99)
    speed = random.randrange(0, 10)
    temperature = random.randrange(20, 30)
    
    data = dict()
    data["location"] = LOCATION_CODE
    data["timestamp"] = ts
    data["direction"] = direction
    data["humidity"] = humidity
    data["speed"] = speed
    data["temperature"] = temperature
    return data
