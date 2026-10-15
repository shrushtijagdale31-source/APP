
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create customer data
data = {
    "CustomerID": [101, 102, 103, 104, 105, 106],
    "Tenure": [2, 12, 24, 5, 36, 8],
    "MonthlyCharges": [500, 800, 600, np.nan, 900, 700],
    "Contract": ["Monthly", "Yearly", "Yearly",
                 "Monthly", "Yearly", "Monthly"],
    "Churn": ["Yes", "No", "No", "Yes", "No", "Yes"]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Customer Data:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df["MonthlyCharges"] = df["MonthlyCharges"].fillna(
    df["MonthlyCharges"].mean()
)

# Remove duplicate records
df = df.drop_duplicates()

print("\nCleaned Customer Data:")
print(df)

# Generate summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Count customers who left and stayed
print("\nCustomer Churn Count:")
print(df["Churn"].value_counts())

# Calculate churn percentage using NumPy
churn = np.sum(df["Churn"] == "Yes")
total = len(df)
percentage = (churn / total) * 100

print("\nChurn Percentage:", percentage, "%")

# Create scatter plot
plt.scatter(df["Tenure"], df["MonthlyCharges"])
plt.title("Customer Tenure vs Monthly Charges")
plt.xlabel("Tenure (Months)")
plt.ylabel("Monthly Charges")
plt.show()

# Create bar graph
df["Churn"].value_counts().plot(kind="bar")
plt.title("Customer Churn Count")
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")
plt.show()

# Compare churn by contract
pd.crosstab(df["Contract"], df["Churn"]).plot(kind="bar")
plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.show()

