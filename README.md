# IoT_Raspberry_Docker_GPIO

Used in a Raspberry Pi 3 v1.2

# Docker
[Docker comes to Raspberry Pi](https://www.raspberrypi.org/blog/docker-comes-to-raspberry-pi/)

```curl -sSL https://get.docker.com | sh```

##### Adding Docker group
```sudo usermod -aG docker $USER```

##### Installing docker-compose
```sudo pip install docker-compose```

# GPIO Library
## Pre-requisite
Share the GPIO devices ```/dev/gpiomem```. 
It is already done in the ```docker-compose.yml```.

## Library used
[WiringPi - Python](https://github.com/WiringPi/WiringPi-Python)

# Data exploitation
All data that is readed from the GPIO ports is uploaded to an API REST.

[IoT Simple API - Firebase](https://iot-simple-api.firebaseio.com/data.json)
