# Loan-Approval-Prediction
Kaggle competition Loan Approval Prediction

# Loan Approval Prediction

This project is part of the Kaggle competition on Loan Approval Prediction. The goal of the project is to build a machine learning model that can predict whether a loan application will be approved or not based on various features of the applicants.

## Table of Contents

- [Introduction](#introduction)
- [Data Analysis](#data-analysis)
- [Modeling](#modeling)
- [Hyperparameter Tuning](#hyperparameter-tuning)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

The Loan Approval Prediction project aims to provide insights into the factors affecting loan approval and to create a predictive model using historical data of loan applications. The dataset consists of various features such as applicant information, loan details, and previous repayment history.

## Data Analysis

Data analysis was performed using the following libraries:

- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **Seaborn & Matplotlib**: For data visualization and generating informative graphs.

The analysis included:
- Exploratory data analysis (EDA) to understand data distributions and relationships.
- Visualization of trends and patterns in the data.

## Modeling

The following machine learning algorithms were implemented:

1. **Logistic Regression**: A statistical method for predicting binary classes.
2. **Decision Tree Classifier**: A model that uses a tree-like structure to make decisions based on feature values.
3. **Random Forest Classifier**: An ensemble learning method that fits multiple decision trees and combines their predictions.

## Hyperparameter Tuning

To improve the performance of the models, hyperparameter tuning was performed using:

- **Grid Search Cross-Validation (GridSearchCV)**: This technique was used to systematically test a range of hyperparameter values to find the optimal settings for each model.

## Installation

To run this project, you will need to have Python and the following libraries installed:

```bash
pip install pandas numpy seaborn matplotlib scikit-learn
```
--------------------------------------------------------------------------------
# Neural model (neural_loan notebook)

## Loan Status Prediction Project

## Overview

This project aims to predict the status of loan applications using neural networks implemented in Keras, TensorFlow. The goal is to develop an accurate model that can classify loans as approved or rejected based on various features.

### Dataset

### Dataset Source
playground-series folder

## Description:

The Loan Approval Prediction project aims to provide insights into the factors affecting loan approval and to create a predictive model using historical data of loan applications. The dataset consists of various features such as applicant information, loan details, and previous repayment history.

## Project Structure

data/
data.csv (raw dataset)
notebook/ neural_loan.pynb
best_model.h5 (saved model with optimal hyperparameters)
README.md (this file)

## Methodology

Data Preprocessing
Data transformation: handling missing values, encoding categorical variables, and scaling/normalizing features.
Data splitting: dividing the preprocessed data into training (80%) and validation sets (20%).

## Model Development
Built a baseline neural network model using Keras, TensorFlow.
Implemented hyperparameter tuning using GridSearchCV.

## Model Evaluation
Evaluated the performance of the optimal model on the validation set.
Predicted loan status for new, unseen data.
Models
Baseline Model: A simple neural network model with default hyperparameters.
Optimal Model: The best-performing model obtained through hyperparameter tuning using GridSearchCV.
Requirements
Python 
TensorFlow
Keras
Scikit-learn
Pandas
NumPy
Matplotlib/Seaborn (for visualization)

## Usage
Clone the repository.
Install required libraries.
Run Data_Preprocessing.ipynb to transform and split the data.
Run Loan_Status_Prediction.ipynb to develop and evaluate the models.
Future Work
Explore other machine learning algorithms.
Feature engineering.
Collect additional data.

## License
MIT

## Author

Ayebazibwe Ishmael

Feel free to modify this template to better suit your project's specific needs.

