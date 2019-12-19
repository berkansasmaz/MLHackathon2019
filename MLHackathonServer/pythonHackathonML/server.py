# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, render_template, make_response
from sklearn.externals import joblib
import traceback
import pandas as pd
import json
import requests
import random
import time
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['Post'])
def yorumlar():
    yorum = request.args.get('link', default = '*', type = str)
   
        
    if model:
        
        #json_ = request.form['data']
        print(yorum)

       
        
        print("aa:"+json.dumps(json_)+"\n")
        #query = pd.get_dummies(pd.DataFrame(json_))

        prediction = model.predict([yorum])

        resp = jsonify({'prediction': str(prediction)})
        # response = app.response_class(response=json.dumps(prediction),mimetype='application/json')
     
        print(prediction)
        return str(prediction)
        
            
       
    
  #  imdbUrl =request.args.get('link', default = 1, type = str)
   # imdbUrl='https://www.hepsiburada.com/hometech-alfa-110a-intel-atom-z3735f-2gb-32gb-emmc-windows-10-home-11-6-fhd-tasinabilir-bilgisayar-p-HBV00000BEEWD'
   # yorum = request.args.get('yorum', default = '*', type = str)
   
    
                                 

        
    

    
    
    



if __name__ == '__main__':

	model = joblib.load("latest_model.pkl")# Load "model.pkl"
	print('Model loaded')
app.run(debug=True)
