# Importing needed libraries

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.preprocessing import scale
from sklearn import metrics


# read the CSV file into a DataFrame
loan_data = pd.read_csv('Loan_Default.csv')

# Insert both numerical and categorical features

numerical_columns = [
    'loan_amount',
    'rate_of_interest',
    'Interest_rate_spread',
    'Upfront_charges',
    'term',
    'property_value',
    'income',
    'Credit_Score',
    'LTV',
    'dtir1'
]

categorical_columns = [
    'loan_limit',
    'Gender',
    'approv_in_adv',
    'loan_type',
    'loan_purpose',
    'Credit_Worthiness',
    'open_credit',
    'business_or_commercial',
    'Neg_ammortization',
    'interest_only',
    'lump_sum_payment',
    'construction_type',
    'occupancy_type',
    'Secured_by',
    'total_units',
    'credit_type',
    'age',
    'submission_of_application',
    'Region'
]

# Impute missing values in the categorical features using the 'most_frequent' strategy
imputer = SimpleImputer(strategy='most_frequent')
loan_data[categorical_columns] = imputer.fit_transform(loan_data[categorical_columns])

# Impute missing values in the numerical features using the column mean
loan_data[numerical_columns] = loan_data[numerical_columns].fillna(loan_data[numerical_columns].mean())

# Create a boolean mask indicating which values are NaN
mask = loan_data[categorical_columns].isna()

# Checking weather any of the values in the mask has missing value
if mask.any().any():
    print('There are NaN values in the columns.')
else:
    print('There are no NaN values in the columns.')

# One-hot encoding for categorical features only
cat_feat = pd.get_dummies(loan_data[categorical_columns])

df_no_status = loan_data[numerical_columns].join(cat_feat)

# Converting all cat. labels to the ordinary array
key_list = df_no_status.columns.tolist()

# Creating a pandas DataFrame with both cat. and num. features
new_loan_data = df_no_status.join(loan_data[['Status']])

# Standardizing dataframe without 'Status' for future training
X_scaled = pd.DataFrame(scale(df_no_status))

# Target
Y = loan_data[['Status']]

X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2)

# Using LogaritmicRegression for training as output (y) can be only 0 or 1
LogReg = LogisticRegression()
LogReg.fit(X_train, Y_train)

prediction_test = LogReg.predict(X_test)
print('Accuracy: =>', metrics.accuracy_score(Y_test, prediction_test))

feature_names = df_no_status.columns
coefs = list(zip(LogReg.coef_[0], feature_names))

# Sorting the list in descending order by coefficient value
coefs = sorted(coefs, key=lambda x: x[0], reverse=True)

# Getting the top 10 highest values
top_10 = coefs[:10]

for coef in top_10:
    print(f'{coef[1]}: {coef[0]}')
