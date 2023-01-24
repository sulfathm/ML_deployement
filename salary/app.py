# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 23:26:48 2023

@author: user pc
"""

from flask import Flask , request ,render_template
import pickle
import numpy as np
import pandas as pd

app=Flask(__name__)
model=pickle.load(open("model.pkl",'rb'))
@app.route("/")

def home():
    return render_template('salary.html')

@app.route('/predict',methods=['POST'])
def predict():
    salary=float(request.values['text'])
    a=pd.DataFrame({"salary":[salary]})
    print(a)
    y_pred=model.predict(a)
    y_pred
    # salary=np.reshape(salary,(-1,1))
    # output=model.predict(salary)
    # output=output.item()
    # output=round(output,2)
    
    
    return render_template ('salary.html',prediction_text="salary amount is {} ".format(y_pred))
if __name__=='__main__':
    app.run()