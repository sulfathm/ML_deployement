# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 12:18:04 2023

@author: user pc
"""

from flask import Flask , request , render_template
import pickle
import numpy as np
import pandas as pd

app=Flask(__name__)
model=pickle.load(open('weathermodel.pkl','rb'))
@app.route("/")


def home():
    return render_template("weather.html")

@app.route("/predict",methods=['POST'])
def predict():
    precipitation=(request.values['text1'])
    temp_max=(request.values['text2'])
    temp_min=(request.values['text3'])
    wind=(request.values['text4'])
    
    a=pd.DataFrame({"precipitation":[precipitation],
                    "temp_max":[temp_max],
                    "temp_min":[temp_min],
                    "wind":[wind]})
    print(a)
    y_prediction=model.predict(a)
    print(y_prediction)
    
    if y_prediction==([0]):
        prediction="drizzle"
    elif y_prediction==([1]):
        prediction="fog"
    elif y_prediction==([2]):
        prediction="rain"
    elif y_prediction==([3]):
        prediction="sun"
    else:
        prediction="cold"
    
    return render_template ("result.html", prediction_text="The weather is {} ".format(prediction))
if __name__=="__main__":
    app.run()
    
     
    