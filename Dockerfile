FROM python:3.10-slim-bullseye
ENV PYTHONUNBUFFERED=1
WORKDIR /PumpuySkyline

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install tk

COPY . .