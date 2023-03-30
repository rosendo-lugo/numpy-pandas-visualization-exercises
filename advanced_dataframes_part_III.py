# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercises III
# Use your get_db_url function to help you 
# explore the data from the chipotle database.
import pandas as pd
import numpy as np
from env import get_db_url # This allows you to find the get_db_url function from the env.py file. 
# from pydataset import data


# get the data from MySQL
# The below lines allow you to communicate with MySQL and retrive tables.
# This retrives the orders table from the Chipotle database
# If you need to change databases and tables just update "chipotle (database) and orders (table)"
url = get_db_url('chipotle') # Chipotle is the database were the orders table is coming from. Don't forget that Chipotle is a database not a table.
orders_table = pd.read_sql('SELECT * FROM orders', url) # Orders is a table. The table is located in the mySQL
print('\n',orders_table)


# 1. What is the total price for each order?
print('\nExercises III, Question 1')

# url = get_db_url('chipotle')
# query = '''
# SELECT order_id, SUM(CAST(REPLACE(item_price, '$', '') AS DECIMAL(10,2))) AS total_price
# FROM orders
# GROUP BY order_id
# '''

# total_price_df = pd.read_sql(query, url)
# print(total_price_df)

# pd.pivot_table(data=total_price_df, index='order_id', values='item_price', aggfunc='sum') 


# clean the item_price column
orders_table['item_price'] = orders_table['item_price']\
    .str.replace('$', '').astype(float)

# pivot the data to get the total price for each order
order_totals = pd.pivot_table(orders_table, values='item_price',\
                               index='order_id', aggfunc=np.sum)

print(order_totals)
# 2. What are the most popular 3 items?
print('\nExercises III, Question 2')
popular_three = orders_table.groupby('item_name')['quantity'].sum()
top_three = popular_three.sort_values(ascending=False).head(3)
print(f'Option 1\n',top_three)


# print(orders_table.head())
most_popular = pd.pivot_table(data=orders_table, index='item_name', values='quantity', aggfunc='sum')
three_popular = most_popular.nlargest(3, 'quantity')
print(f'\nOption 2\n',three_popular)



# 3. Which item has produced the most revenue?
print('\nExercises III, Question 3')

# Use the pivot_table() method to group orders by item_name and order_id
#  and sum the quantity and item_price columns for each group
order_totals = pd.pivot_table(orders_table, index='item_name',\
                               values=['quantity', 'item_price'], aggfunc=np.sum)


# Created another column named "total_price" by multipling the quantity and item price
order_totals['total_price'] = order_totals['quantity'] * order_totals['item_price']

# Use the nlargest() method to return the row with the highest total item_price
most_revenue = order_totals.nlargest(1, 'total_price')

print(f'The item with the most Revenue\n',most_revenue)


# 4. Join the employees and titles DataFrames together.
print('\nExercises III, Question 4')


# 5. For each title, find the hire date of the employee
# that was hired most recently with that title.
print('\nExercises III, Question 5')


# 6. Write the code necessary to create a cross tabulation
# of the number of titles by department. (Hint: this 
# will involve a combination of SQL code to pull the 
# necessary data and python/pandas code to perform the
# manipulations.)
print('\nExercises III, Question 6')





