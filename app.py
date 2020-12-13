import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
from tweet_processing import similar_tweets

arr = pickle.load(open('arr.pkl', 'rb'))
arr_og = pickle.load(open('arr_og.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    output = ''

    if len(str(*request.form.values())) > 1:

        output = similar_tweets(str(*request.form.values()), arr, arr_og)
        
        affichage = str()

        for i in range(len(output['tweet'])):
            affichage = affichage + 'Score: ' + str(output['cosine'][i]) + ' | Tweet: ' + output['tweet'][i] + '<br><br>'

        if affichage:
            return render_template('index.html', prediction_text='Top 20 Tweets : <br><br>' + affichage)
        else:
            return render_template('index.html', prediction_text='No matching tweets found')
    
    else:
        
        return render_template('index.html', prediction_text='Please enter a valid sentence')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)