FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /workspace/

COPY src/main.py /workspace/

RUN apt update \
    && apt install make -y\
    && apt install python3 -y\
    && apt install python3-pip -y\
    && apt install openjdk-11-jdk-headless -qq -y\
    && apt install scala -y\
    && apt install git -y\
    && python3 main.py

COPY Makefile Dockerfile requirements.txt /workspace/

RUN make install

COPY . /workspace/