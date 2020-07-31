FROM python:3.7-slim
RUN apt-get update
RUN apt-get install -y build-essential
RUN pip install django==2.2.13 channels==2.4.0 channels_redis==2.4.2
WORKDIR /proj
