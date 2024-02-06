#!/usr/bin/env python3
'''flask for routes'''


from flask import Flask, render_template


app = Flask("__name__")


@app.route('/')
def index():
    '''fucntion to call our index.html'''
    return rnder_template('index.html')
if __name == "__main--":
    app.run(debug=True)
