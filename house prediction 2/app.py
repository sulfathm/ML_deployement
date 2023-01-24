# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=['POST'])
def predict():
    area=float(request.values['area'])
    print(area)
    area=np.reshape(area,(-1,1))
    output=model.predict(area)
    output=output.item()
    output=round(output,2)
    
    
    return render_template('index.html',prediction_text="price for the house is ${}".format(output))
if __name__=='__main__':
    app.run(port=8000)