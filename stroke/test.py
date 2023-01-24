# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 00:50:42 2023

@author: user pc
"""

from flask import Flask , request , render_template
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)
model=pickle.load(open("model.pkl","rb"))
@app.route("/")

def home():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():
    Gender=int(request.values['text1'])
    
    print(Gender)
        
    return render_template("result.html",prediction_text="The patient {} .".format("prediction"))
if __name__=="__main__":
    app.run()
    