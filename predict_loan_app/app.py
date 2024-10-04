from flask import Flask, render_template, request
from joblib import load
import pandas as pd

app = Flask(__name__)

model = load('loan_approval_model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            form_data = {
                'person_age': int(request.form['person_age']),
                'person_income': int(request.form['person_income']),
                'person_home_ownership': request.form['person_home_ownership'],
                'person_emp_length': int(request.form['person_emp_length']),
                'loan_intent': request.form['loan_intent'],
                'loan_grade': request.form['loan_grade'],
                'loan_amnt': int(request.form['loan_amnt']),
                'loan_int_rate': float(request.form['loan_int_rate']),
                'loan_percent_income': float(request.form['loan_percent_income']),
                'cb_person_default_on_file': request.form['cb_person_default_on_file'],
                'cb_person_cred_hist_length': int(request.form['cb_person_cred_hist_length']),
            }

            print("Form Data Received:", form_data)

            input_data = pd.DataFrame([form_data])
            prediction = model.predict(input_data)

            prediction_str = "predction null"
            if prediction[0] == 0:
                prediction_str = 'No'
            else:
                prediction_str = 'Yes'

            return render_template('index.html', prediction= str(prediction_str))

        except Exception as e:
            print(f"Error: {e}")
            return render_template('index.html', prediction="Error in prediction")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)