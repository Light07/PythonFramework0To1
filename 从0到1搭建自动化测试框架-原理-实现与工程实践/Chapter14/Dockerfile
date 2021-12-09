FROM jenkins/jenkins:lts
USER root
RUN mkdir /my_app
WORKDIR /my_app
COPY requirements.txt /my_app
RUN pwd
RUN ls -la

RUN apt-get update && apt-get install -y \
    software-properties-common
RUN apt-get update && apt-get install -y \
    git \
    python3.9 \
    python3-pip

