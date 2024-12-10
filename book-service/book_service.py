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
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    title = data.get('title')
    author = data.get('author')
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Book added!'}), 201

@app.route('/books', methods=['GET'])
def get_books():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM books')
    rows = c.fetchall()
    conn.close()
    books_list = [{'id': r[0], 'title': r[1], 'author': r[2]} for r in rows]
    return jsonify({'books': books_list}), 200

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()
    app.run(host='0.0.0.0', port=5001)