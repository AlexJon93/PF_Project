from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='http://localhost:8080')

from . import db

@app.route('/')
def get():
    orders = db.get_orders()
    return jsonify(orders)

if __name__ == "__main__":
    app.run()