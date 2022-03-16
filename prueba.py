from flask import Flask, redirect,render_template, request
import pandas as pd
import csv
app = Flask(__name__)
@app.route("/", methods = ['GET','POST'])
#@app.route("/home", methods = ['GET','POST'])

def home():
    return render_template("index.html")
@app.route("/data", methods = ['GET','POST'])
def upload_page():
    return render_template("upload.html")
@app.route("/market")
def market_page():
    items  = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}]
    return render_template("market.html",items = items)
if __name__ == '__main__':

    app.run('0.0.0.0',5000,debug=True)