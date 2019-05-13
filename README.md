# IoT_Raspberry_Docker_GPIO

Used in a Raspberry Pi 3 v1.2. The main goal is to push data to the cloud from GPIO sensors connected to the Raspberry. And at the same time, the second goal is to have all the code running in microservices, Docker. Also using Google Firebase Realtime Database.

# Schematic

![First schematic](https://raw.githubusercontent.com/LaQuay/IoT_Raspberry_Docker_GPIO/master/img/esquematic_1.png)
*The module used in this project is the FC-37, but it is similar to YL-83*

### Specification of FC-37
- Analog (Not tested)
   - 0 is Wet
   - 1023 is Dry
- Digital
   - LOW (0) is for Wet
   - HIGH (1) is for Dry
- Vcc - 5V
- GND - GND
- A0 - Not connected
- D0 - GPIO 3 (Pinout 5)

## Docker
[Docker comes to Raspberry Pi](https://www.raspberrypi.org/blog/docker-comes-to-raspberry-pi/)

```curl -sSL https://get.docker.com | sh```

##### Adding Docker group
```sudo usermod -aG docker $USER```

##### Installing docker-compose
```sudo pip install docker-compose```

## GPIO Library
### Pre-requisite
Share the GPIO devices ```/dev/gpiomem```. 
It is already done in the ```docker-compose.yml```.

### Library used
[WiringPi - Python](https://github.com/WiringPi/WiringPi-Python)

## Data exploitation
All data that is readed from the GPIO ports is uploaded to an API REST.

[IoT Simple API - Firebase](https://iot-simple-api.firebaseio.com/data.json)
