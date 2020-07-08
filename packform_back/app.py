from flask import Flask, jsonify

app = Flask(__name__)

from . import db

@app.route('/')
def get():
    orders = db.get_orders()
    return jsonify(orders)

if __name__ == "__main__":
    app.run()