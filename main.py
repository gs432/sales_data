import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# MySQL connection
myDB = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = 'Gstra@249',
    database = 'sales_data'
)


# Load table into pandas dataframe
df = pd.read_sql('SELECT * FROM orders', con=myDB)


# data cleaning and preprocessing
# calculate total revenue
revenue_by_product = df.groupby('product_name')['quantity', 'product_price'].agg({
    'quantity': 'sum',
    'product_price': 'mean'
}).reset_index()
revenue_by_product['revenue'] = revenue_by_product['quantity'] * revenue_by_product['product_price']


# create barchart
plt.figure(figsize=(10, 5))
sns.barplot(x='product_name', y='revenue', data=revenue_by_product)
plt.title('Total Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue ($)')
plt.show()