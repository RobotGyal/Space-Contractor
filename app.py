from flask import Flask, request, render_template, redirect, url_for
import os 
from bson.objectid import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient

#framework initializing 
app = Flask(__name__)
load_dotenv()
client = MongoClient('localhost', 27017)
db = client.space

# sets up databases
space_items = db.space_items    #sets up space items as a database
cart_items = db.cart_items      #items for user to add to cart from space items
cart_items.drop()

space_items = [
    {'title': 'Bubble Mask', 'description':'Vacuum Face Mask', 'price': '3000 sc', 'image': './static/bubble.jpg'},
    {'title': 'Towel', 'description':'For all needs', 'price': '42 sc'},
    {'title': 'Forcefield', 'description': 'Protect from outside intrusion', 'price': '5,000,000 sc'}
]


# Main route
@app.route('/')
def home():
    '''Main page setup function'''
    return render_template('homepage.html', space_items=space_items)


#Route for VIEWING store items on homepage
@app.route('/store', methods=['GET'])
def store_display():
    return render_template('store_display.html', space_items=space_items)


# ~~~~~~~~  CART  ~~~~~~~~
# methods=['GET']
# VIEWING cart homepage
@app.route('/cart')
def cart_display():
    return render_template('cart_display.html', cart_items=cart_items.find())

# ADD items to cart
@app.route('/cart/add')
def devices_new():
    '''Create devices'''
    return render_template('cart_add.html')

# Route for POSTING items to cart
@app.route('/cart', methods=['POST'])
def cart_post():
    '''Submit items to cart'''
    cart= {
        'title': request.form.get('title'),
        'description': request.form.get('description')
    }
    cart_id =cart_items.insert_one(cart).inserted_id
    return redirect(url_for('cart_display', cart_id=cart_id)) 

# Route to VIEW items in cart
@app.route('/cart/<cart_id>')
def cart_show(cart_id):
    """Show a single cart item."""
    cart = cart_items.find_one({'_id': ObjectId(cart_id)})
    return render_template('cart_display.html', cart_items=cart_items, cart=cart)

# #DELETE
# @app.route('/cart_items/<cart_id>/delete', methods=['POST'])
# def cart_delete(cart_id):
#     """Delete one playlist."""
#     cart_items.delete_one({'_id': ObjectId(cart_id)})
#     return redirect(url_for('cart_display', cart_id=cart_id))


if __name__=='__main__':
    app.run(Debug = True)