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

