# Take reference to the following example: 
# https://docs.aws.amazon.com/iot/latest/developerguide/iot-moisture-raspi-setup.html
#
# Documentation for AWSIoTPythonSDK:
# https://github.com/aws/aws-iot-device-sdk-python

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from .settings import *

# Init AWSIoTMQTTClient
aws_client = None
aws_client = AWSIoTMQTTClient(CLIENT_ID)
aws_client.configureEndpoint(HOST, PORT)
aws_client.configureCredentials(ROOT_CA, KEY, CERT)

# AWSIoTMQTTClient connection configuration
aws_client.configureAutoReconnectBackoffTime(1, 32, 20)
aws_client.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
aws_client.configureDrainingFrequency(2)  # Draining: 2 Hz
aws_client.configureConnectDisconnectTimeout(10)  # 10 sec
aws_client.configureMQTTOperationTimeout(5)  # 5 sec
