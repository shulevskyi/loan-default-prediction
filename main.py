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
# sns.distplot(df['Credit_Score'], hist=False)
# # Highlighted mean of Credit_Score on the plot
# plt.axvline(df['Credit_Score'].mean(), color='r', linestyle='--', label='Mean')
# # Highlighted mode of Credit_Score on the plot
# plt.axvline(df['Credit_Score'].mode()[0], color='g', linestyle='--', label='Mode')
#
# plt.legend()
# plt.show()
#
# # Correlation between rate_of_interest and loan_amount graphically
# sns.regplot(x=df['rate_of_interest'], y=df['loan_amount'], fit_reg=True, line_kws={'color': 'black'},
#             scatter_kws={'color': 'blue'})
# plt.show()

# Mean values of income for each Gender
# df.groupby('Gender')['income'].mean().plot(kind='bar')
# plt.show()

# Annual Salary distribution per default status:
# plt.figure(figsize=(12, 6))
# plt.hist(df[df['Status'] == 1]['income'], histtype='step', bins=1000, label='Defaulted')
# plt.hist(df[df['Status'] == 0]['income'], histtype='step', bins=1000, label='Not Defaulted')
# Difference between the two distributions in percentege under the highers graph plt.text(0, 0.5, str(round((df[df[
# 'Status'] == 1]['income'].mean() - df[df['Status'] == 0]['income'].mean()) / df[df['Status'] == 0]['income'].mean()
# * 100, 2)) + '%', fontsize=20)
# Shade The Area Between Two Lines In A Line Chart
# plt.fill_between([0, 100000], [0, 0], [0, 0.0005], color='red', alpha=0.2)
# plt.xlim(0, 60000)
# plt.title('Figure 4: Annual Salary distribution by Default status')
# plt.legend()
# plt.show()

# print the second row of Status
print(df['loan_amount'][1])
print(features_col)



