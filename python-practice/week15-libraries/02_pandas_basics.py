# Week 15: External Libraries - pandas for Data Analysis
# Run: python3 week15-libraries/02_pandas_basics.py
# Install: pip install pandas

import pandas as pd
import json


print("=== pandas - Data Analysis Library ===\n")

# Creating a DataFrame from dictionary
print("--- Creating DataFrame ---")
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "age": [25, 30, 35, 28, 32],
    "city": ["New York", "London", "Paris", "Tokyo", "Berlin"],
    "salary": [70000, 80000, 75000, 85000, 72000]
}
df = pd.DataFrame(data)
print(df)
print()


# Basic DataFrame info
print("--- DataFrame Info ---")
print(f"Shape: {df.shape}")  # (rows, columns)
print(f"Columns: {list(df.columns)}")
print(f"Data types:\n{df.dtypes}")
print()


# Accessing data
print("--- Accessing Data ---")
print("First 3 rows:")
print(df.head(3))
print("\nLast 2 rows:")
print(df.tail(2))
print("\nSpecific column:")
print(df["name"])
print("\nMultiple columns:")
print(df[["name", "age"]])
print()


# Filtering data
print("--- Filtering Data ---")
print("People older than 30:")
print(df[df["age"] > 30])
print("\nPeople from New York or London:")
print(df[df["city"].isin(["New York", "London"])])
print("\nPeople older than 28 with salary > 70000:")
print(df[(df["age"] > 28) & (df["salary"] > 70000)])
print()


# Statistics
print("--- Statistics ---")
print("Describe numeric columns:")
print(df.describe())
print(f"\nAverage age: {df['age'].mean():.1f}")
print(f"Average salary: ${df['salary'].mean():,.2f}")
print(f"Max salary: ${df['salary'].max():,}")
print(f"Min age: {df['age'].min()}")
print()


# Adding new columns
print("--- Adding Columns ---")
df["bonus"] = df["salary"] * 0.1
df["total_compensation"] = df["salary"] + df["bonus"]
print(df[["name", "salary", "bonus", "total_compensation"]])
print()


# Sorting
print("--- Sorting ---")
print("Sort by age (ascending):")
print(df.sort_values("age")[["name", "age"]])
print("\nSort by salary (descending):")
print(df.sort_values("salary", ascending=False)[["name", "salary"]])
print()


# Grouping
print("--- Grouping ---")
# Add department column for grouping example
df["department"] = ["IT", "HR", "IT", "HR", "IT"]
print("Average salary by department:")
print(df.groupby("department")["salary"].mean())
print("\nCount by department:")
print(df.groupby("department").size())
print()


# Reading from CSV
print("--- Reading/Writing CSV ---")
# Create sample CSV
df.to_csv("employees.csv", index=False)
print("✅ Saved to employees.csv")

# Read it back
df_loaded = pd.read_csv("employees.csv")
print("Loaded from CSV:")
print(df_loaded.head())
print()


# Reading from JSON
print("--- Reading/Writing JSON ---")
df.to_json("employees.json", orient="records", indent=2)
print("✅ Saved to employees.json")

df_json = pd.read_json("employees.json")
print("Loaded from JSON:")
print(df_json.head())
print()


# Handling missing data
print("--- Handling Missing Data ---")
# Create DataFrame with missing values
data_with_nulls = {
    "name": ["Alice", "Bob", "Charlie", None, "Eve"],
    "age": [25, None, 35, 28, 32],
    "score": [85, 90, None, 88, 92]
}
df_nulls = pd.DataFrame(data_with_nulls)
print("DataFrame with missing values:")
print(df_nulls)
print(f"\nMissing values per column:\n{df_nulls.isnull().sum()}")

# Fill missing values
df_filled = df_nulls.fillna({"age": df_nulls["age"].mean(), "score": 0, "name": "Unknown"})
print("\nAfter filling missing values:")
print(df_filled)
print()


# Applying functions
print("--- Applying Functions ---")
# Apply function to column
df["age_category"] = df["age"].apply(lambda x: "Young" if x < 30 else "Senior")
print(df[["name", "age", "age_category"]])
print()


# Practical example: Analyzing data
print("--- Practical Analysis ---")
sales_data = {
    "product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Laptop", "Mouse", "Keyboard"],
    "quantity": [2, 5, 3, 1, 1, 8, 2],
    "price": [1000, 25, 75, 300, 1000, 25, 75],
    "date": ["2024-01-01", "2024-01-01", "2024-01-02", "2024-01-02", "2024-01-03", "2024-01-03", "2024-01-03"]
}
sales_df = pd.DataFrame(sales_data)
sales_df["total"] = sales_df["quantity"] * sales_df["price"]

print("Sales Data:")
print(sales_df)

print("\nTotal sales by product:")
product_sales = sales_df.groupby("product")["total"].sum().sort_values(ascending=False)
print(product_sales)

print(f"\nTotal revenue: ${sales_df['total'].sum():,}")
print(f"Average order value: ${sales_df['total'].mean():.2f}")
print(f"Most sold product: {sales_df.groupby('product')['quantity'].sum().idxmax()}")
print()


# Merging DataFrames
print("--- Merging DataFrames ---")
employees = pd.DataFrame({
    "emp_id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "dept_id": [10, 20, 10]
})

departments = pd.DataFrame({
    "dept_id": [10, 20, 30],
    "dept_name": ["IT", "HR", "Sales"]
})

merged = pd.merge(employees, departments, on="dept_id")
print("Merged employee and department data:")
print(merged)
print()


# TODO: Load a CSV file and calculate statistics
# TODO: Create a DataFrame from a list of dictionaries
# TODO: Filter data based on multiple conditions
# TODO: Group data and calculate aggregates (sum, mean, count)
# TODO: Create a pivot table from sales data


# Useful pandas operations:
# - df.head(n) - First n rows
# - df.tail(n) - Last n rows
# - df.info() - DataFrame info
# - df.describe() - Statistics
# - df[column] - Select column
# - df[df[column] > value] - Filter rows
# - df.sort_values(column) - Sort
# - df.groupby(column) - Group data
# - df.fillna(value) - Fill missing values
# - df.dropna() - Drop rows with missing values
# - pd.merge(df1, df2) - Merge DataFrames
# - df.to_csv(file) - Save to CSV
# - pd.read_csv(file) - Load from CSV
