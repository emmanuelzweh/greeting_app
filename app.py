
from flask import Flask, flash, render_template, request, sessions
import sqlite3

from sqlalchemy import true

app = Flask(__name__)
app.secret_key = "dfjldeojkddn46dksfk"

@app.route('/')
def home():
    flash('What is your name?')
    return render_template('index.html')

@app.route('/greet', methods = ['POST', 'GET'])
def greet():
    flash(f"Hi {request.form['name_input']}, great to see you!")
    request.form['name_input']
    return render_template('index.html')
    


if __name__ == "__main__":
    app.run(debug=true)