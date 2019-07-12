from flask import *
import os

app = Flask(__name__)

@app.route('/')

def hello_world():
    return "Hello World."

@app.route('/home',methods=['POST','GET'])

def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()