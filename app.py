#!/usr/bin/env python
 # -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    with open('counter.txt', 'r') as f:
        counter = f.read()
    return '{}'.format(counter)


@app.route('/stat')
def counter_increment():
    with open('counter.txt', 'r') as f:
        counter = f.read()
    new_counter = int(counter) + 1
    with open('counter.txt', 'w') as f:
        f.write(str(new_counter))
    return '{}'.format(counter)

@app.route('/about')
def about():
    return "<h3> Hello , Irina</h3"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
