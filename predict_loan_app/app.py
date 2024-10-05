from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
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

            input_data = pd.DataFrame([form_data])
            prediction = model.predict(input_data)

            prediction_str = 'Yes' if prediction[0] == 1 else 'No'

            return render_template('index.html', prediction=prediction_str)

        except Exception as e:
            print(f"Error: {e}")
            return render_template('index.html', prediction="Error in prediction")

    return render_template('index.html')


# DATABASE 

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Load_database.db"
db = SQLAlchemy(app)

# Define your database model
class Loan_Data(db.Model):
    id = db.Column(db.Integer, nullable=False)
    # Add columns as per your CSV file structure
    person_age = db.Column(db.Integer, nullable=False)
    person_income = db.Column(db.Integer, nullable=False)
    person_home_ownership = db.Column(db.String(20), nullable=False)
    person_emp_length = db.Column(db.Integer, nullable=False)
    loan_intent = db.Column(db.String(30), nullable=False)
    loan_grade = db.Column(db.String(10), nullable=False)
    loan_amnt = db.Column(db.Integer, nullable=False)
    loan_int_rate = db.Column(db.Float, nullable=False)
    loan_percent_income = db.Column(db.Float, nullable=False)
    cb_person_default_on_file = db.Column(db.String(10), nullable=False)
    cb_person_cred_hist_length = db.Column(db.Integer, nullable=False)
    loan_status = db.Column(db.String(10), nullable=False)


# Create database and tables
with app.app_context():
    db.create_all()

file_path = 'C:/Users/ISHMO_CT/Downloads/my-projects/nueral_env/Loan-Approval-Prediction/playground-series-s4e10/train.csv'
# Load CSV file
def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df

# Insert data into database
def insert_data(df):
    for index, row in df.iterrows():
        new_row = Loan_Data(
            id =row['id'],
            person_age=row['person_age'],
            person_income=row['person_income'],
            person_home_ownership=row['person_home_ownership'],
            person_emp_length=row['person_emp_length'],
            loan_intent=row['loan_intent'],
            loan_grade=row['loan_grade'],
            loan_amnt=row['loan_amnt'],
            loan_int_rate=row['loan_int_rate'],
            loan_percent_income=row['loan_percent_income'],
            cb_person_default_on_file=row['cb_person_default_on_file'],
            cb_person_cred_hist_length=row['cb_person_cred_hist_length'],
            loan_status=row['loan_status']
        )
        db.session.add(new_row)
    db.session.commit()

# Route to insert data
@app.route("/insert-data", methods=["POST"])
def insert_data_route():
    file_path = 'C:/Users/ISHMO_CT/Downloads/my-projects/nueral_env/Loan-Approval-Prediction/playground-series-s4e10/train.csv'  # Update file path
    df = load_csv(file_path)
    insert_data(df)
    return "Data inserted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
