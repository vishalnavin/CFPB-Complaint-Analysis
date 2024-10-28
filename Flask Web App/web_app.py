# -*- coding: utf-8 -*-
"""
@author: Saumitra
"""

from flask import Flask, request, render_template
from joblib import load

app = Flask(__name__)

# Load pre-trained model and TF-IDF vectorizer
model = load('model.pkl')
tfidf = load('tfidf.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Collect data from the form
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        complaint = request.form['complaint']

        # Transform the complaint to TF-IDF format
        complaint_tfidf = tfidf.transform([complaint])

        # Predict the product category
        prediction = model.predict(complaint_tfidf)
        product = prediction[0]  # Assuming the prediction is properly interpreted

        # Render the template with all the collected and processed data
        return render_template('home.html', name=name, email=email, phone=phone, complaint=complaint,
                               prediction_text=f'{product}', submitted=True)
    else:
        # Initial page load without any POST data
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
