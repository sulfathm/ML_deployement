# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 23:12:48 2023

@author: user pc
"""

from flask import Flask , request , render_template
import pickle
import numpy as np
import pandas as pd

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route("/")


def home():
    return render_template("house.html")

@app.route("/predict",methods=['POST'])
def predict():
    BHK=(request.values['text1'])
    size=(request.values['text2'])
    bedroom=(request.values['text3'])
    
    # g=int(input("BHK"))
    # h=int(input("Size"))
    # i=int(input("Bathroom"))

    a=pd.DataFrame({"BHK":[BHK],
                "Size":[size],
                "Bathroom":[bedroom]})
    print(a)
    y_pred=model.predict(a)
    print(y_pred)


# def size():
#     size=float(request.values['text'])
#     BHk=np.reshape(size,(-1,1))
#     output=model.predict(size)
#     output=output.item()
#     output=round(output,2)
    
# def bedroom():
#     bedroom=float(request.values['text'])
#     bedroom=np.reshape(bedroom,(-1,1))
#     output=model.predict(bedroom)
#     output=output.item()
#     output=round(output,2)
    
    return render_template("result.html",prediction_text="The rent amount is{} ".format(y_pred))
if __name__=="__main__":
    app.run()
    