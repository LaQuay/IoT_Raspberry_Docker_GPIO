# Pull base image
FROM python:3
MAINTAINER Marc Vila <hola@marcvila.me>

# Install wiringPi for GPIO
RUN pip install wiringpi

# Install request for HTTP requests
RUN pip install requests

ENV LANG C.UTF-8
ENV PYTHONIOENCODING UTF-8