FROM python:latest

WORKDIR app
COPY requirements.txt requirements.txt
COPY code/consumer.py consumer.py
COPY code/templates/index.html templates/index.html
RUN pip3 install -r requirements.txt

ENV FLASK_APP consumer
EXPOSE 80
ENTRYPOINT flask run -h 0.0.0.0 -p 80
