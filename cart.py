

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

PRODUCT_SERVICE_URL = 'https://product-service-ppqh.onrender.com' 

@app.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    # Simulate fetching the user's cart from the Cart Service
    return jsonify({'user_id': user_id, 'cart': []})

@app.route('/cart/<int:user_id>/add/<int:product_id>', methods=['POST'])
def add_to_cart(user_id, product_id):
    # Simulate adding a product to the user's cart
    return jsonify({'message': f'Product {product_id} added to cart'})

@app.route('/cart/<int:user_id>/remove/<int:product_id>', methods=['POST'])
def remove_from_cart(user_id, product_id):
    # Simulate removing a product from the user's cart
    return jsonify({'message': f'Product {product_id} removed from cart'})

if __name__ == '__main__':
    app.run(debug=True)
