#!/usr/bin/python

'''
Q5: Below is some starter code for a Flask Web Application. Expand on that and include a
    route that simulates rolling two dice and returns the result in JSON. You should include
    a brief explanation of your code.

Answer:
'''

from flask import Flask, jsonify
app = Flask(__name__)

import json
import random

@app.route('/')
def dice():
    dice1 = str(random.randint(1,6))
    dice2 = str(random.randint(1,6))

    return jsonify(diceone = dice1, dicetwo = dice2)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)