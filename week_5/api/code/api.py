import random

from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOSTNAME = os.environ.get("POSTGRES_HOSTNAME")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")

if __name__ == "__main__":
    app.run()


@app.route('/api/v1/recommend_meal')
def recommend():
    conn = psycopg2.connect(database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PASSWORD,
                            host=POSTGRES_HOSTNAME, port=POSTGRES_PORT)
    cursor = conn.cursor()
    cursor.execute('''SELECT * from public.meals''')
    rows = cursor.fetchall()
    row = random.choice(rows)
    columns = ['name', 'price']
    response = dict(zip(columns, row[1:]))
    return jsonify(response)
