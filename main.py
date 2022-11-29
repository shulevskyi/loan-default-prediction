import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import missingno as msno
import seaborn as sns

df = pd.read_csv("Loan_Default.csv")

features_col = df.columns.values.tolist()  # Converting all column's labels to the list

count_row = df.shape[0]  # Gives number of row count

df_temp = df.copy()

# percentage of missing values in each column
print(str(df_temp.isnull().sum() * 100 / len(df_temp)) + " %")

# Percentage distribution histogram of Credit_Score
sns.distplot(df['Credit_Score'], hist=False)
# Highlighted mean of Credit_Score on the plot
plt.axvline(df['Credit_Score'].mean(), color='r', linestyle='--', label='Mean')
# Highlighted mode of Credit_Score on the plot
plt.axvline(df['Credit_Score'].mode()[0], color='g', linestyle='--', label='Mode')

plt.legend()
plt.show()

# Correlation between rate_of_interest and loan_amount graphically
sns.regplot(x=df['rate_of_interest'], y=df['loan_amount'], fit_reg=True, line_kws={'color': 'black'},
            scatter_kws={'color': 'blue'})
plt.show()
