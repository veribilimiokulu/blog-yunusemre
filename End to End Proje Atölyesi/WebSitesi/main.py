from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import pickle
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',sonuc_basari="", sonuc_olumsuz="")

@app.route('/sonuc',methods=['POST'])
def sonuc():
    model = model = pickle.load(open('static/base-model.sav', 'rb'))

    input_1 = request.form['EXT_SOURCE_3']
    input_2 = request.form['DAYS_LAST_PHONE_CHANGE']
    input_3 = request.form['DAYS_CREDIT']
    input_4 = request.form['EXT_SOURCE_2']
    input_5 = request.form['AMT_CREDIT_x']
    input_6 = request.form['AMT_ANNUITY_x']

    input_array = np.array([float(input_1),float(input_2),float(input_3),float(input_4),float(input_5),float(input_6)])
    input_array = input_array.reshape(1, -1)
    y_pred = model.predict(input_array)
    
    print(y_pred)
    
    if y_pred == 1:
        return render_template('index.html',sonuc_basari="Krediniz Onaylanmıştır.",sonuc_olumsuz="")

    if y_pred == 0:
        return render_template('index.html',sonuc_olumsuz="Krediniz Onaylanmamıştır.",sonuc_basari="")

    

if __name__=='__main__':
	app.run(debug=True,port=8080)

