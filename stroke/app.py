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
    Gender=(request.values['text1'])
    Age=float(request.values['text2'])
    HyperTension=float(request.values['text3'])
    Heardisease=float(request.values['text4'])
    MaritalStatus=float(request.values['text5'])
    Averageglucoselevel=float(request.values['text6'])
    BMI=float(request.values['text7'])
    Smokingstatus=float(request.values['text8'])
    df=pd.DataFrame({"Gender":[Gender],
                     "Age":[Age],
                     "HyperTension":[HyperTension],
                     "Heardisease":[Heardisease],
                     "MaritalStatus":[MaritalStatus],
                     "Averageglucoselevel":[Averageglucoselevel],
                     "BMI":[BMI],
                     "Smokingstatus":[Smokingstatus]})
    y_prediction=model.predict(df)
    print(y_prediction)
    
    
    if y_prediction==([0]):
        prediction="doesn't have stroke"
        return render_template("result.html",prediction_text="The patient {} .".format(prediction))
    else:
        prediction="have stroke"
        return render_template("result1.html",prediction_text="The patient {} .".format(prediction))
        
    
if __name__=="__main__":
    app.run()
    