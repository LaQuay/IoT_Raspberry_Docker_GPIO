import wiringpi
import requests

BASE_URL = "https://iot-simple-api.firebaseio.com/"

def sendData(sensor_name, sensor_value):
    url = BASE_URL + "data.json"
    data = {
        "name": sensor_name,
        "value": sensor_value,
        "timestamp": ""
    }
    print("Sending data..." + url + str(data))
    print("URL: " + url)
    print(str(data))
    
    r = requests.post(url, json=data)
    print("Data sent... "+ str(r.status_code) + " " + str(r.reason))

print("Starting script...")

# Set up GPIO pin numbering
wiringpi.wiringPiSetupGpio()

# Read pin 6
pin_value = wiringpi.digitalRead(6)

print("Pin 6: " + str(pin_value))

sendData("Test", "288")

