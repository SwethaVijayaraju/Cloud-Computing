import random
from flask import Flask, jsonify
import socket


app = Flask(__name__)

MEALS = [
    {'name': 'Masala Dosa', 'price': 9.99},
    {'name': 'Ramen', 'price': 13.50},
    {'name': 'Pop Corn Chicken', 'price': 11.99},
    {'name': 'Chilli Chicken', 'price': 12.99},
    {'name': 'Biriyani', 'price': 12.99},
    {'name': 'Beans Parupu Usuli', 'price': 7.99},
    {'name': 'Medu Vada', 'price': 6.50},
    {'name': 'Grilled Chicken Burger', 'price': 8.99},
    {'name': 'South Indian Filter Coffee', 'price': 5.00},
    {'name': 'Chicken Buritto', 'price': 9.99},
    {'name': 'Basil Pasta', 'price': 10.99},
    {'name': 'Idly Vada Pongal Combo', 'price': 10.99},
    {'name': 'Fried Rice', 'price': 9.99},
    {'name': 'Apple Pie', 'price': 9.99},
    {'name': 'Enchilada', 'price': 10.50},
]


@app.route('/api/v1/recommend_meal')
def recommend():
    meal = random.choice(MEALS)
    meal['api_hostname'] = socket.gethostname()
    return jsonify(meal)


app.run()
