from flask import Flask, request, render_template
import os 
from dotenv import load_dotenv
from pymongo import MongoClient

#framework initializing 
app = Flask(__name__)
load_dotenv()
client = MongoClient('localhost', 27017)
db = client.space
space_items = db.space_items    #sets up space items as a database

# Main route
@app.route('/')
def test():
    '''Main page setup function'''
    return render_template('store_index.html', space_items=space_items.find())


if __name__=='__main__':
    app.run(Debug = True)