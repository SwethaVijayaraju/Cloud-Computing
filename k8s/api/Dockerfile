FROM python:latest

WORKDIR app
COPY requirements.txt requirements.txt
COPY code/api.py api.py
RUN pip3 install -r requirements.txt

ENV FLASK_APP api
EXPOSE 5000
ENTRYPOINT flask run -h 0.0.0.0 -p 5000
