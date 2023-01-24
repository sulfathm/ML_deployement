# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask , request , render_template
import pickle
import numpy as np

app=Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route("/")

def home():
    return render_template('tip.html')
@app.route('/predict',methods=['POST'])
def predict():
    tip=float(request.values['text'])
    tip=np.reshape(tip,(-1,1))
    output=model.predict(tip)
    output=output.item()
    output=round(output,2)
    
    return render_template('tip.html',prediction_text="Price for the house is ${} ".format(output))
    
if __name__=='__main__':
    app.run()