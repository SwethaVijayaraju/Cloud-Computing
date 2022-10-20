import random
import time

from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOSTNAME = os.environ.get("POSTGRES_HOSTNAME")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")


def init_db():
    while True:
        print("Initializing DB")
        try:
            conn = psycopg2.connect(database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PASSWORD,
                                    host=POSTGRES_HOSTNAME, port=POSTGRES_PORT)
            cursor = conn.cursor()
            cursor.execute(open("init.sql", "r").read())
            print("Successfully initialized DB")
            return conn
        except Exception as e:
            print("Error initializing to DB")
            print(e)
            print("Try again in 5 seconds")
            time.sleep(5)


@app.route('/api/v1/recommend_meal')
def recommend():
    cursor = conn.cursor()
    cursor.execute('''SELECT * from public.meals''')
    rows = cursor.fetchall()
    row = random.choice(rows)
    columns = ['name', 'price']
    response = dict(zip(columns, row[1:]))
    return jsonify(response)

app.run()
conn = init_db()
