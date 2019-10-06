from flask import Flask, request, render_template
import os 

#framework initializing 
app = Flask(__name__)

#Main route
@app.route('/')
def test():
    '''Main page setup function'''
    return "The page works"


if __name__=='__main__':
    app.run(Debug = True)