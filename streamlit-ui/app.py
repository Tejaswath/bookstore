import streamlit as st
import requests

st.title("Bookstore App")

BOOK_SERVICE_URL = 'http://book-service:5001'
ORDER_SERVICE_URL = 'http://order-service:5002'

st.header("Manage Books")

with st.form(key='add_book_form'):
    title = st.text_input("Title")
    author = st.text_input("Author")
    submit_book = st.form_submit_button("Add Book")

if submit_book:
    resp = requests.post(f'{BOOK_SERVICE_URL}/books', json={'title': title, 'author': author})
    if resp.status_code == 201:
        st.success("Book added!")
    else:
        st.error("Failed to add book.")

if st.button("View Books"):
    r = requests.get(f'{BOOK_SERVICE_URL}/books')
    if r.status_code == 200:
        st.write(r.json()['books'])
    else:
        st.error("Failed to retrieve books.")

st.header("Manage Orders")

with st.form(key='place_order_form'):
    book_id = st.number_input("Book ID", min_value=1)
    quantity = st.number_input("Quantity", min_value=1)
    submit_order = st.form_submit_button("Place Order")

if submit_order:
    r = requests.post(f'{ORDER_SERVICE_URL}/orders', json={'book_id': int(book_id), 'quantity': int(quantity)})
    if r.status_code == 201:
        st.success("Order placed!")
    else:
        st.error("Failed to place order.")

if st.button("View Orders"):
    r = requests.get(f'{ORDER_SERVICE_URL}/orders')
    if r.status_code == 200:
        st.write(r.json()['orders'])
    else:
        st.error("Failed to retrieve orders.")