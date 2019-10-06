from flask import Flask, request, render_template
import os 
from dotenv import load_dotenv

#framework initializing 
app = Flask(__name__)
load_dotenv()

#Main route
@app.route('/')
def test():
    '''Main page setup function'''
    return "The page works"


if __name__=='__main__':
    app.run(Debug = True)