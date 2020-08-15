import json
import subprocess
import time
import traceback

from .cloud import aws_client
from .dummy_data import generate_random_data
from .settings import TOPIC

# Publish to TOPIC
while True:
    try:
        subprocess.call("sudo pon internet") # replace internet with the name of the connection script
        time.sleep(5)
        aws_client.connect() 
        data = generate_random_data()
        # logic for getting data from sqlite
        message = json.dumps(data)
        aws_client.publish(TOPIC, message, 1)
        print('Published topic %s: %s\n' % (TOPIC, message))
        aws_client.disconnect()
        subprocess.call("sudo poff internet") # turn off internet connection to save power
        time.sleep(300)
    except:
        traceback.print_exc()
