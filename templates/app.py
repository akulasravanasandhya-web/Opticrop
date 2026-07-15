from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained ML model
try:
    with open('crop_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            N = float(request.form['N'])
            P = float(request.form['P'])
            K = float(request.form['K'])
            temp = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            ph = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])
            
            input_features = np.array([[N, P, K, temp, humidity, ph, rainfall]])
            
            if model:
                prediction = model.predict(input_features)[0]
                return render_template('index.html', prediction_text=f"Our system recommends growing: {prediction.upper()}")
            else:
                return render_template('index.html', prediction_text="Model file not found. Please train the model first.")
        except Exception as e:
            return render_template('index.html', prediction_text="Error in input data. Please check values.")

if __name__ == "__main__":
    app.run(debug=True)
  
