# Pull base image
FROM python:3
MAINTAINER Marc Vila <hola@marcvila.me>

# Install wiringPi
RUN pip install wiringpi

ENV LANG C.UTF-8
ENV PYTHONIOENCODING UTF-8