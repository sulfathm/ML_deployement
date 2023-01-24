# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask,render_template,request
import pickle
import numpy as np
app=Flask(__name__)
model = pickle.load(open("model.pkl",'rb'))
@app.route("/")

def home():
    return render_template("salary.html")
@app.route("/predict", methods=['POST'])
def predict():
    
    print("hello")
    return render_template('index.html',prediction_text="price for the house is ${}")
if __name__=='__main__':
    app.run(port=8000)