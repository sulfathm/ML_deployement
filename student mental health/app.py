# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 20:55:43 2023

@author: user pc
"""

from flask import Flask , render_template , request
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
    Age=(request.values['text2'])
    Year_of_study=(request.values['text3'])
    CGPA=(request.values['text4'])
    Marital_status=(request.values['text5'])
    Depression=(request.values['text6'])
    Anxiety=(request.values['text7'])
    Treatment=(request.values['text8'])
    
    df=pd.DataFrame({"Gender":[Gender],
                 "Age":[Age],
                 "Year_of_study":[Year_of_study],
                 "CGPA":[CGPA],
                 "MArital_status":[Marital_status],
                 "Depression":[Depression],
                 "Anxiety":[Anxiety],
                 
                 "Treatment":[Treatment]})
    # Gender=(request.values['text1'])
    # Age=float(request.values['text2'])
    # Year_of_study=float(request.values['text3'])
    # CGPA=float(request.values['text4'])
    # Marital_Status=float(request.values['text5'])
    # Depression=float(request.values['text6'])
    # Anxiety=float(request.values['text7'])
    # Treatment=float(request.values['text8'])
    # df=pd.DataFrame({"Gender":[Gender],
    #              "Age":[Age],
    #              "Year_of_study":[Year_of_study],
    #              "CGPA":[CGPA],
    #              "MArital_status":[Marital_status],
    #              "Depression":[Depression],
    #              "Anxiety":[Anxiety],
                 
    #              "Treatment":[Treatment]})
    print(df)
    
    y_prediction=model.predict(df)
    print(y_prediction)
    
    if y_prediction==([1]):
        prediction="Panick attack!"
        return render_template("result1.html",prediction_text="The student will affect {} .".format(prediction))
    else:
        prediction=" safe from panick attack!!"
        return render_template("result2.html",prediction_text="The student {} .".format(prediction))
if __name__=="__main__":
     app.run()
    
        
    