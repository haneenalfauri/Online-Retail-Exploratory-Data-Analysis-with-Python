import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file_path = "Online Retail.xlsx"
df = pd.read_excel(file_path, sheet_name="Online Retail")

#Plotting a simple line plot
plt.plot(df['Quantity'], df['UnitPrice'])
plt.xlabel('Quantity')
plt.ylabel('Unit Price')
plt.title('Quantity vs Unit Price')
plt.show()


# Display the first few rows of the dataset to get an initial look at the data
print("First few rows of the dataset:")
print(df.head())

# Check for any missing values in the dataset
print("\nMissing values in each column:")
print(df.isnull().sum())

# Remove rows where CustomerID is missing, as it's important for our analysis
df = df.dropna(subset=['CustomerID'])

# Replace any missing descriptions with an empty string to keep the data consistent
df['Description'] = df['Description'].fillna('')

# Remove any duplicate rows to ensure our dataset is clean
df = df.drop_duplicates()

# Convert negative quantities to positive values
df['Quantity'] = df['Quantity'].abs()

#Check and remove any item with price <=0
unit_price_zero_count = df[df['UnitPrice'] <= 0].shape[0]
print(f"Number of rows with Unit Price equal to 0: {unit_price_zero_count}")

# Drop rows where UnitPrice is equal to 0
df = df[df['UnitPrice'] > 0]





# Display basic statistics of the dataset for a quick overview
print("\nBasic statistics of the dataset:")
print(df.describe())


# Set the plot style to make the visualizations look nice
sns.set(style="whitegrid")

# Convert quantities to thousands
df['Quantity'] = df['Quantity'] / 1000

# Plot a histogram of the 'Quantity' column to see its distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Quantity'], bins=50, kde=True)
plt.title('Distribution of Quantity (in Thousands)')
plt.xlabel('Quantity (in Thousands)')
plt.ylabel('Frequency')
plt.show()

# Create a scatter plot to visualize the relationship between 'UnitPrice' and 'Quantity'


# Plot the scatter plot of Unit Price vs Quantity
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Quantity', y='UnitPrice', data=df)
plt.title('Unit Price vs Quantity (in Thousands)')
plt.xlabel('Quantity (in Thousands)')
plt.ylabel('Unit Price')
plt.show()

# Plot a bar chart of the top 10 countries by total quantity sold
top_countries = df.groupby('Country')['Quantity'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_countries.index, y=top_countries.values)
plt.title('Top 10 Countries by Quantity Sold')
plt.xlabel('Country')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=45)
plt.show()

# Analyze Sales Trends Over Time
# Convert the InvoiceDate column to datetime format for easier manipulation
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Extract the month and day of the week from the InvoiceDate
df['Month'] = df['InvoiceDate'].dt.month
df['DayOfWeek'] = df['InvoiceDate'].dt.dayofweek

# Analyze monthly sales trends by grouping the data by month and summing the quantities sold
monthly_sales = df.groupby('Month')['Quantity'].sum()

# Plot the monthly sales trend
plt.figure(figsize=(10, 6))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values)
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Quantity Sold')
plt.show()

# Analyze weekly sales trends by grouping the data by day of the week and summing the quantities sold
weekly_sales = df.groupby('DayOfWeek')['Quantity'].sum()

# Plot the sales trend by day of the week
plt.figure(figsize=(10, 6))
sns.lineplot(x=weekly_sales.index, y=weekly_sales.values)
plt.title('Sales Trend by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Total Quantity Sold')
plt.xticks(ticks=range(7), labels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
plt.show()


# Identify the top 10 selling products based on the total quantity sold
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)

# Plot the top 10 selling products
plt.figure(figsize=(12, 6))
sns.barplot(x=top_products.index, y=top_products.values)
plt.title('Top 10 Selling Products')
plt.xlabel('Product Description')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=45)
plt.show()

# Task 7: Identify Outliers and Anomalies
# Use a box plot to identify outliers in the 'Quantity' column
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Quantity'])
plt.title('Box Plot of Quantity')
plt.xlabel('Quantity')
plt.show()


print("\nConclusions and Summary of Findings:")
print("- The dataset contains transactions from various countries, with the UK being the top contributor.")
print("- The majority of transactions involve small quantities, with a few transactions having very high quantities, indicating potential outliers.")
print("- The most sold products include various decorative and household items.")
print("- Sales peak during certain months and days of the week, with higher sales observed during weekdays.")

