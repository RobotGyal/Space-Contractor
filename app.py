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
space_items = db.space_items    #sets up space items as a database

home_items = [
    {'title': 'Bubble Mask', 'description':'Vacuum Face Mask', 'price': '3000 sc'},
    {'title': 'Towel', 'description':'For all needs', 'price': '42 sc'},
    {'title': 'Forcefield', 'description': 'Protect from outside intrusion', 'price': '5,000,000 sc'}
]


# Main route
@app.route('/')
def test():
    '''Main page setup function'''
    return render_template('store_index.html', space_items=space_items.find())


#Route for VIEWING store items on homepage
@app.route('/store')
def store_display():
    return render_template('store_display.html', home_items=home_items)


# Route for VIEWING to cart
@app.route('/store/cart', methods=['GET'])
def cart_display():
    return render_template('cart_display.html') 

# Route for ADDING to cart
@app.route('/store/cart', methods=['POST'])
def cart_submit():
    '''Add items to cart'''
    space_item = {
    'title': request.form.get('title'),
    'description': request.form.get('description'),
    'price': request.form.get('price'),
    }
    space_item_id = space_items.insert_one(space_item).inserted_id
    return redirect(url_for('cart_items_show', space_item_id=space_item_id))

#Show cart items
@app.route('/store/cart/<space_items_id>')
def playlists_show(playlist_id):
    space_item = space_items.find_one({'_id': ObjectId(space_item_id)})
    return render_template('cart_display.html', space_item=space_item)


if __name__=='__main__':
    app.run(Debug = True)