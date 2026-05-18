

# Customer Churn & Retention Analysis

## Introduction

This project analyzes customer churn data to identify retention trends, churn patterns, and customer behavior in a subscription-based business.

## Objective

- Identify churn patterns
- Analyze customer retention
- Understand customer behavior
- Generate business insights

## Tools Used

- Python
- Google Colab
- Pandas
- Matplotlib
- Seaborn

# Importing Required Libraries

The required Python libraries are imported for data analysis and visualization.

- Pandas is used for data handling and preprocessing.
- Matplotlib is used for creating charts and graphs.
- Seaborn is used for advanced data visualizations.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['figure.figsize'] = (10,5)

"""# Loading the Dataset

The customer churn dataset is loaded into the notebook using Pandas.

The dataset contains:
- Customer demographics
- Subscription details
- Monthly charges
- Contract information
- Churn status
"""

df = pd.read_csv('/content/WA_Fn-UseC_-Telco-Customer-Churn.csv')

"""# Dataset Overview

The first few rows of the dataset are displayed to understand the structure and available columns.

Dataset information and statistical summaries are also analyzed.
"""

df.head()

df.info()

df.describe()

"""# Data Cleaning

The dataset is checked for:
- Missing values
- Duplicate records
- Data consistency

Data cleaning improves analysis accuracy.
"""

df.isnull().sum()

df.drop_duplicates(inplace=True)

"""# Customer Churn Distribution

This analysis compares customers who stayed with the company and customers who left the service.
"""

sns.countplot(x='Churn', data=df)

plt.title("Customer Churn Distribution")

plt.show()

"""# Monthly Charges vs Customer Churn

This visualization analyzes whether higher monthly charges influence customer churn.
"""

sns.boxplot(x='Churn', y='MonthlyCharges', data=df)

plt.title("Monthly Charges vs Churn")

plt.show()

"""# Contract Type Analysis

This analysis identifies which contract types have higher churn rates.
"""

sns.countplot(x='Contract', hue='Churn', data=df)

plt.title("Contract Type vs Churn")

plt.xticks(rotation=10)

plt.show()

"""# Customer Tenure Analysis

Customer tenure analysis helps understand how long customers stay active before churning.
"""

sns.histplot(data=df, x='tenure', hue='Churn', bins=30)

plt.title("Customer Tenure Distribution")

plt.show()

"""# Internet Service Analysis

This visualization compares churn rates across different internet service categories.
"""

sns.countplot(x='InternetService', hue='Churn', data=df)

plt.title("Internet Service vs Churn")

plt.show()

"""# Churn Rate Calculation

The churn rate measures the percentage of customers who discontinued the service.
"""

churn_rate = (df['Churn'].value_counts()['Yes'] / len(df)) * 100

print("Churn Rate: {:.2f}%".format(churn_rate))

"""# Key Insights

- Customers with month-to-month contracts showed higher churn.
- Higher monthly charges were associated with increased churn.
- Customers with longer tenure were more likely to stay.
- Fiber optic internet users showed relatively higher churn rates.

# Recommendations

- Encourage customers to choose long-term contracts.
- Provide loyalty offers for high-risk customers.
- Improve support services for customers with high monthly charges.
- Develop retention campaigns for new customers.

# Conclusion

This analysis successfully identified customer churn patterns, retention drivers, and customer behavior trends.

The generated insights can help subscription-based businesses improve customer retention and reduce customer loss.
"""