# pull official base image
FROM python:3.9.5-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# updated
# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql make sox pkg-config libavcodec-dev libavformat-dev libavresample-dev libavutil-dev libsndfile1-dev libsamplerate-dev librubberband-dev libvorbis-dev libflac-dev \
  && apt-get clean 

# install dependencies
RUN pip install --upgrade pip
RUN pip install ipython
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# add app
COPY ./ ./usr/src/app

