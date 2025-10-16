from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def map():
    return render_template('main.html')