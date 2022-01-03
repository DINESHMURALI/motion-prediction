# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 15:51:41 2022

@author: Admin
"""

from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)
Model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['post'])
def predict():
    X = float(request.form['X'])
    Y = float(request.form['Y'])
    Z = float(request.form['Z'])
    result = Model.predict([[X, Y, Z]])[0]
    return render_template('index.html', prediction = result)



if __name__ == "__main__":
    app.run(debug=True)
    