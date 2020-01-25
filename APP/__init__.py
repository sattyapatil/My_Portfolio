
from flask import Flask, render_template


app = Flask(__name__, template_folder='./build', static_folder='./build')


@app.route('/')
def index():

    return render_template('index.html')


