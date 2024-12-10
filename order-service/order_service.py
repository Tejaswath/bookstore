from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

DATABASE = '/app/shared/bookstore.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY(book_id) REFERENCES books(id)
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/orders', methods=['POST'])
def place_order():
    data = request.json
    book_id = data.get('book_id')
    quantity = data.get('quantity')

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('INSERT INTO orders (book_id, quantity) VALUES (?, ?)', (book_id, quantity))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Order placed!'}), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM orders')
    rows = c.fetchall()
    conn.close()
    orders_list = [{'id': r[0], 'book_id': r[1], 'quantity': r[2]} for r in rows]
    return jsonify({'orders': orders_list}), 200

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()
    else:
        init_db()
    app.run(host='0.0.0.0', port=5002)