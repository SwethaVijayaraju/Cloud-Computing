from flask import Flask, render_template
import http.client
import os
import json

API_HOST = os.environ.get("API_HOST")
API_PORT = os.environ.get("API_PORT")
API_ENDPOINT = os.environ.get("API_ENDPOINT")

app = Flask(__name__)


@app.route('/')
def recommend():
    connection = http.client.HTTPConnection(API_HOST + ":" + API_PORT)
    connection.request('GET', API_ENDPOINT)
    response = connection.getresponse()
    meal = json.loads(response.read().decode())
    return render_template('index.html', meal=meal)


if __name__ == "__main__":
    app.run()

