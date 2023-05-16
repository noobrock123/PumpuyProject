FROM python:3.10-slim-bullseye
ENV PYTHONUNBUFFERED=1
# Check Your directory
WORKDIR /PUMPUYPROJECT

COPY requirements.txt requirements.txt
COPY manage.py manage.py
RUN pip3 install -r requirements.txt

# For Linux
# RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# RUN apt-get install tk

# For Windows
# replace with container ID
# Copy command run in terminal
# docker exec -it container id python manage.py makemigrations
# docker exec -it container id python manage.py migrate

COPY . .