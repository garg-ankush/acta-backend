FROM python:3.8.6-slim-buster

RUN pip install --upgrade pip && \
    pip --version

RUN apt-get update && \
    apt-get install -y --no-install-recommends git build-essential gcc cmake

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app
EXPOSE 5000

CMD python api.py
