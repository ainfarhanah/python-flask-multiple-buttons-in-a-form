from flask import Flask, send_file, render_template, request
import os
import glob
import pandas as pd
import datetime

app = Flask('__name__')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/annyeongz', methods = ['GET', 'POST'])
def submit():
    if request.method == "POST":
        if request.form.get("wonyoung"):
            return render_template('wonyoung.html')
        elif request.form.get("yujin"):
            return render_template('yujin.html')
    elif request.method == "GET":
        return 'failed'
