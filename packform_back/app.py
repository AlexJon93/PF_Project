from flask import Flask, jsonify

app = Flask(__name__)

from . import db

@app.route('/')
def get():
    # customers = db.get_customer('ivan')
    orders = db.get_orders()
    return jsonify(orders)

if __name__ == "__main__":
    app.run()

# sample_order = {
#         'order_name': 'PO #001-I', 
#         'customer_company': 'Roga & Kopyta', 
#         'customer_name': 'Ivan Ivanovich', 
#         'order_date': '2020-01-02T15:34:12Z', 
#         'delivered_amount': 99.11,
#         'total_amount': 99.11
#     }