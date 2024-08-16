import pandas as pd

df = pd.read_csv('./files/sales_records.csv')  # Read CSV data into dataframe. Pandas automatically uses the first row as column names

print("df.describe()")
print(df.describe())  # Get statistics on the numeric columns (use `df.describe(include='O')` for text columns)
print("="*20)

print('df.info()')
print(df.info())  # Get information on all the columns ('object' means text/string)
print("="*20)

print('df.head(5)')
print(df.head(5))  # Display first 5 rows of the dataframe (`df.describe(__n__)` displays n rows)
print("="*20)

print("df['total_sales'] = df['Units Sold'] * df['Unit Price']")
df['total_sales'] = df['Units Sold'] * df['Unit Price']
print(df)
print("="*20)

print("df.info()")
print(df.info())
print("="*20)
print("df.describe()")
print(df.describe())
print("="*20)

