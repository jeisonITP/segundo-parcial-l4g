import mysql.connector

from flask import Flask, render_template

db = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= '',
    port= 3306
)

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/crear')
def crear():
    return render_template('crear.html')

app.run(debug=True)
