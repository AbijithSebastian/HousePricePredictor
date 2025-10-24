from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

# Base directory of your project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load ML objects
model = pickle.load(open(os.path.join(BASE_DIR, 'backend', 'model.pkl'), 'rb'))
preprocessor = pickle.load(open(os.path.join(BASE_DIR, 'backend', 'preprocessor.pkl'), 'rb'))
poly = pickle.load(open(os.path.join(BASE_DIR, 'backend', 'poly.pkl'), 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    age = float(request.form['age'])
    location = request.form['location']

    input_df = pd.DataFrame([[area, bedrooms, age, location]],
                            columns=['Area', 'Bedrooms', 'Age', 'Location'])
    
    processed = preprocessor.transform(input_df)
    poly_processed = poly.transform(processed)
    prediction = model.predict(poly_processed)[0]

    return render_template('index.html',
                           result=f"Estimated Price: ₹{round(prediction,2)}")

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
