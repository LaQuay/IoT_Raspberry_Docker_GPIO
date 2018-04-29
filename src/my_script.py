import wiringpi
import requests
from datetime import datetime

# Pinout
# https://docs.microsoft.com/en-us/windows/iot-core/media/pinmappingsrpi/rp2_pinout.png

BASE_URL = "https://iot-simple-api.firebaseio.com/"
HIGH = 1
LOW = 0
OUTPUT = 1
INPUT = 0

def sendData(sensor_name, sensor_value, sensor_observation=""):
    url = BASE_URL + "data.json"
    data = {
        "name": sensor_name,
        "value": sensor_value,
        "timestamp": str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        "observations": sensor_observation
    }
    print("Sending data...")
    print(str(data))
    
    r = requests.post(url, json=data)
    print("Data sent... "+ str(r.status_code) + " " + str(r.reason))
    
# D0 of sensor placed in GPIO3 (5 pinout)
# Sends a 1 if rain is detected
# Sends a 0 if rain is not detected
def readRainSensor():
    pin = 3
    wiringpi.pinMode(pin, INPUT)  
    pin_value = wiringpi.digitalRead(pin)

    print("Pin " + str(pin) + ": " + str(pin_value))
    if pin_value:
        pin_value = 0
        observation = "No rain detected"
    else:
        pin_value = 1
        observation = "Rain detected"
    print("Observation: " + str(observation))

    sendData("Rain Sensor", str(pin_value), str(observation))

print("Starting script...")

# Set up GPIO pin numbering
wiringpi.wiringPiSetupGpio()

readRainSensor()

