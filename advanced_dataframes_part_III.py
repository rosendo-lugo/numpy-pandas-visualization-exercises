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
orders_table_df = pd.read_sql('SELECT * FROM orders', url) # Orders is a table. The table is located in the mySQL
print('\n',orders_table_df)


# 1. What is the total price for each order?
print('\nExercises III, Question 1')

# ************** Option 1 **************
query = '''
SELECT order_id, SUM(CAST(REPLACE(item_price, '$', '') AS DECIMAL(10,2))) AS total_price
FROM orders
GROUP BY order_id
'''

total_price_df = pd.read_sql(query, url)
print(f'\n************** Option 1 **************\n',total_price_df)


# ************** Option 2 **************
# clean the item_price column
orders_table_df['item_price'] = orders_table_df['item_price']\
    .str.replace('$', '').astype(float)

# pivot the data to get the total price for each order
order_totals = pd.pivot_table(orders_table_df, values='item_price',\
                               index='order_id', aggfunc=np.sum)

print(f'\n************** Option 2 **************\n',order_totals,'\n')



# 2. What are the most popular 3 items?
print('\nExercises III, Question 2')
# ************** Option 1 **************
popular_three = orders_table_df.groupby('item_name')['quantity'].sum()
top_three = popular_three.sort_values(ascending=False).head(3)
print(f'\n************** Option 1 **************\n',top_three)


# ************** Option 2 **************
most_popular = pd.pivot_table(data=orders_table_df, index='item_name', values='quantity', aggfunc='sum')
three_popular = most_popular.nlargest(3, 'quantity')
print(f'\n************** Option 2 **************\n',three_popular) 



# 3. Which item has produced the most revenue?
print('\n\nExercises III, Question 3')
# ONLY ONE OPTION :)

# Use the pivot_table() method to group orders by item_name and order_id
#  and sum the quantity and item_price columns for each group
order_totals = pd.pivot_table(orders_table_df, index='item_name',\
                               values=['quantity', 'item_price'], aggfunc=np.sum)


# Created another column named "total_price" by multipling the quantity and item price
order_totals['total_price'] = order_totals['quantity'] * order_totals['item_price']

# Use the nlargest() method to return the row with the highest total item_price
most_revenue = order_totals.nlargest(1, 'total_price')

print(f'The item with the most Revenue\n\n',most_revenue)


# 4. Join the employees and titles DataFrames together.
print('\nExercises III, Question 4')
url = get_db_url('employees') # Employees is the database were the orders table is coming from.
# Don't forget that Employee is a database not a table.
titles_table_df = pd.read_sql('SELECT * FROM titles', url) # Title is a table. The table is located in the mySQL and was limited to 1000 rows
employees_table_df = pd.read_sql('SELECT * FROM employees', url) # Employees is a table. The table is located in the mySQLL and was limited to 1000 rows
print('\n',titles_table_df.head())
print('\n',employees_table_df.head())

et_tt_merge_df = pd.merge(titles_table_df, employees_table_df, how='', on='emp_no')
print('\n',et_tt_merge_df)

# 5. For each title, find the hire date of the employee
# that was hired most recently with that title.
print('\nExercises III, Question 5')

# Examples of sorting and groupby
# format: pd.merge(df1,df2, how='', on='column_name')
# df.sort_values(by='col1', ascending=False)
# format: df.groupby('column_name').agg_function()
# df.groupby('room').max()[['math','reading','english']]


# titles_table_df.groupby('title').sort()[['from_date']]

# 6. Write the code necessary to create a cross tabulation
# of the number of titles by department. (Hint: this 
# will involve a combination of SQL code to pull the 
# necessary data and python/pandas code to perform the
# manipulations.)
print('\nExercises III, Question 6')





