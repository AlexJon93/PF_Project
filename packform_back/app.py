from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='http://localhost:8080')

from . import db

@app.route('/')
def get():
    search = request.args.get('search')
    date_range = {
        'from_date' : request.args.get('from'),
        'to_date' : request.args.get('to')
    }
    page = int(request.args.get('page')) if request.args.get('page') is not None else 0

    orders = db.get_orders(page, search=search, **date_range)
    return jsonify(orders=orders, pages=db.get_pages())

if __name__ == "__main__":
    app.run()