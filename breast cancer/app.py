# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 10:50:58 2023

@author: user pc
"""

from flask import Flask , request , render_template
import pickle
import numpy as np
import pandas as pd

app=Flask(__name__)
model=pickle.load(open('breastmodel.pkl','rb'))
@app.route("/")


def home():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():
    age=(request.values['text1'])
    menopause=(request.values['text2'])
    tumorsize=(request.values['text3'])
    invnodes=(request.values['text4'])
    degmalig=(request.values['text5'])
    breast=(request.values['text6'])
    Class=(request.values['text7'])

    

    df=pd.DataFrame({"age":[age],
                     "menopause":[ menopause],
                     "tumor size":[tumorsize],
                     "inv nodes":[invnodes],
                     "deg malig":[degmalig],
                     "breast":[breast],
                     "Class":[Class]})
    print(df)
    y_prediction=model.predict(df)
    print(y_prediction)


    if y_prediction==([0]):
        prediction="irradiat"
    else:
        prediction="radiate"
  
  
    return render_template("result.html", prediction_text="The patient is {} ".format(prediction))
if __name__=="__main__":
    app.run() 