from flask import Flask
import random

app=Flask(__name__)

@app.route('/')
def index():
        return 'random: <strong>' +str(random.random())+'</storng>'

@app.route('/create/')
def crete():
        return 'Create'

@app.route('/read/<id>/')
def read(id):
        print(id)
        return 'REad1'+id

app.run(port=5001, debug=True)