import pandas as pd
import numpy as np

np.random.seed(123)

# Create list of values for names column.

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# Randomly generate arrays of scores for each student for each subject.
# Note that all the values need to have the same length here.

math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))


# Construct the DataFrame using the above lists and arrays.

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades,
                   'classroom': np.random.choice(['A', 'B'], len(students))})

# There are several ways to create dataframes, we've already 
# seen how we can create a dataframe from a dictionary:
pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})


# We can also create dataframes from a 2d data structure, 
# either a numpy array or a list of lists:
pd.DataFrame([[1, 2, 3], [4, 5, 6]])

# The array designates the numbers inside the table
# and the next line with the columns in it lables the 
# columns as 'a', 'b', 'c'.
array = np.array([[1, 2, 3], [4, 5, 6]])
pd.DataFrame(array, columns=['a', 'b', 'c'])

# Once those are installed, we can create the connection string. 
# In general, database connection urls will have this format:
from env import host, user, password

url = f'mysql+pymysql://{user}:{password}@{host}/employees'

# Once this url is defined, we can use it with the read_sql function 
# to have pandas treat the results of a SQL query as a dataframe.
pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)

# It is common to have longer SQL queries that we want to read
#  into python, and an example of how we might break a query 
# into several lines is below:

sql = '''
SELECT
    emp_no,
    first_name,
    last_name
FROM employees
WHERE gender = 'F'
LIMIT 100
'''

employees = pd.read_sql(sql, url)
employees.head()


# ******************Passwords and Sensitive Information******************

# Don't add and commit files with passwords or other sensitive 
# information in them to a git repository!

query = '''
SELECT
    t.title as title,
    d.dept_name as dept_name
FROM titles t
JOIN dept_emp USING (emp_no)
JOIN departments d USING (dept_no)
LIMIT 100
'''

title_dept = pd.read_sql(query, url)
title_dept.head()



# Exercises I
# Run python -m pip install pymysql from your terminal to install pymysql.

# Create a notebook or python script named advanced_dataframes to do 
# your work in for these exercises.


# 1. Run python -m pip install pymysql from your terminal to 
# install the mysql client (any folder is fine)
print('Exercises I, Question 1')
print(f'This part was download and installed')

# 2. cd into your exercises folder for this module and 
# run echo env.py >> .gitignore
print('\nExercises I, Question 2')
print(f'The echo env.py >> .gitignore was run')


# 3. Create a function named get_db_url. 
# It should accept a username, hostname, password, and 
# database name and return a url connection string 
# formatted like in the example at the start of this lesson.
print('\nExercises I, Question 3')
# from env import username, password, hostname

from env import user, host, password

def get_db_url(database_name):
    return f"mysql+pymysql://{user}:{password}@{host}/{database_name}"

print(f'this is the function that was created:\n'
   '"def get_db_url(database_name):\n'
        'return f"mysql+pymysql://[user]:[password]@[host]/[database_name]"')

# # 4. Use your function to obtain a connection to the employees database.
print('\nExercises I, Question 4')

employees_table = pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url) 
print('\n',employees_table)

# # 5. Once you have successfully run a query:
# # 5a. Intentionally make a typo in the database url. 
print('\nExercises I, Question 5a')
def get_db_url(database_name):
    return f"mysql+pymysql:{user}:{password}@{host}/{database_name}" #the // were removed after mysql+pymysql

url = get_db_url('employees')
test_employees_table = pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url) 
print('\n',test_employees_table)

# #   What kind of error message do you see?
print(f'This is what I saw:\n'
      'Could not parse rfc1738 URL from string')

# # 5b. Intentionally make an error in your SQL query.
print('\nExercises I, Question 5b')
query = '''
SELECT
    t.title as title,
    d.dept_name as dept_name
FROM titles t
JOIN dept_emp USING (emp_) # On emp_no the 'no' was removed
JOIN departments d USING (dept_no)
LIMIT 100
'''

title_dept = pd.read_sql(query, url)
title_dept.head()
print(title_dept.head())

# #   What does the error message look like?
print(f'This is what I saw:\n'
      'OperationalError: (pymysql.err.OperationalError) (1054, "Unknown column emp_ in ''from' 'clause")')


# # 6. Read the employees and titles tables into two separate DataFrames.
print('\nExercises I, Question 6')

limit_employees_table = pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url) 
print('\n',f'Employees table\n',limit_employees_table)


limit_titles_table = pd.read_sql('SELECT * FROM titles LIMIT 5 OFFSET 50', url) 
print('\n',f'Titles table\n',limit_titles_table)

# # 7. How many rows and columns do you have in each DataFrame? 
# #I'm assuming that is talking about the employees and title tables.
print('\nExercises I, Question 7')
employees_table = pd.read_sql('SELECT * FROM employees', url) 
print('\n',f'Employees table\n',employees_table)


titles_table = pd.read_sql('SELECT * FROM titles', url) 
print('\n',f'Titles table\n',titles_table)

print(f'Employees table',employees_table.shape)
print(f'Titles table',titles_table.shape)
# #   Is that what you expected?
        # Yes


# # 8. Display the summary statistics for each DataFrame.
print('\nExercises I, Question 8')
print(f'Employees table',employees_table.describe())
print(f'Titles table',titles_table.describe())

# # 9. How many unique titles are in the titles DataFrame?
print('\nExercises I, Question 9')
print(f'Titles table',limit_titles_table.title.nunique())
print(f'Titles table',len(limit_titles_table.nunique()))

# # 10. What is the oldest date in the to_date column?
print('\nExercises I, Question 10')
print(f'Titles table',titles_table.to_date.min())

# datetime.date(1985, 3, 1)

# # 11. What is the most recent date in the to_date column?
print('\nExercises I, Question 11')
# datetime.date(1999, 01, 01)

print(f'Titles table',titles_table.to_date.max())

print(f'Titles table',titles_table[titles_table.to_date != titles_table.to_date.max()])

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercises II
# 1. Copy the users and roles DataFrames from the examples above.
print('\nExercises II, Question 1')
print('Both DataFrames were copy')
# Create the users DataFrame.
from pydataset import data
import pandas as pd
import numpy as np


users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
print(f'\nUsers Table\n',users)

# Create the roles DataFrame
roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
print(f'\nRoles Table\n',roles)


# 2. What is the result of using a right join on the DataFrames?
print('\nExercises II, Question 2')

right_join = pd.merge(users,roles, how='right', right_on='id', left_on='role_id', indicator=True)
print(f'Right join\n',right_join)

#Another option
another_option_to_merge = users.merge(roles, how='right', left_on='role_id', right_on='id', indicator=True)
print(another_option_to_merge )

# 3. What is the result of using an outer join on the DataFrames?
print('\nExercises II, Question 3')
outer_join = pd.merge(roles,users, how='outer', right_on='id', left_on='id', indicator=True)
print(f'Outer join\n',outer_join)

# 4. What happens if you drop the foreign keys from 
# the DataFrames and try to merge them?
print('\nExercises II, Question 4')
empty_users = users.drop(columns=['role_id'])
print(f'\nEmpty users table',empty_users)

# empty_roles = roles.drop(columns=['name'])
# print(f'\nEmpty roles table',empty_roles)

empty_outer_join = pd.merge(empty_users,roles, how='outer', right_on='id', left_on='id', indicator=True)
print(f'\nEmpty outer join\n',empty_outer_join)
print(f'\nIt merge both tables but end up changing the last to rows to a left merge\n')

# # 5. Load the mpg dataset from PyDataset.
print('\nExercises II, Question 5')
mpg = data('mpg')
print(f'\nMPG dataset\n',mpg)

# # 6. Output and read the documentation for the mpg dataset.
print('\nExercises II, Question 6')
# print(f'\nMPG dataset\n',mpg, show_doc=True)

# # 7. How many rows and columns are in the dataset?
print('\nExercises II, Question 7')
print(f'\nMPG dataset\n',mpg.shape)

# # 8. Check out your column names and perform any cleanup 
# # you may want on them.
print('\nExercises II, Question 8')
print(f'\nMPG dataset\n',mpg.head())
cars = mpg.rename(columns={'class': 'cls'}, inplace=True)
highway = mpg.rename(columns={'hwy': 'highway'}, inplace=True)
print('\nChanged the cty to city and hwy to highway\n',mpg.head())


# # 9. Display the summary statistics for the dataset.
print('\nExercises II, Question 9')
print(f'\nMPG dataset\n',mpg.describe().T)

# # 10. How many different manufacturers are there?
print('\nExercises II, Question 10')
print(f'\nThe amount of different manufactures: \n',mpg.manufacturer.unique())
print(f'\nThe amount of different manufactures: \n',mpg.manufacturer.nunique())


# # 11. How many different models are there?
print('\nExercises II, Question 11')
print(f'\nmodels\n',mpg.model.unique())
print(f'\nDescribe all\n',mpg.describe(include='all'))

# # 12. Create a column named mileage_difference 
# # like you did in the DataFrames exercises; 
# # this column should contain the difference between
# #  highway and city mileage for each car.
print('\nExercises II, Question 12')

mpg['mileage_difference'] = mpg['highway'] - mpg['cty']
print(mpg.head())

# # 13. Create a column named average_mileage like 
# # you did in the DataFrames exercises; this is the 
# # mean of the city and highway mileage.
print('\nExercises II, Question 13')

mpg[['cty','highway']].agg('mean', axis=1)
mpg['average_mileage'] = mpg[['cty','highway']].agg('mean', axis=1)
print(mpg.head())

# # 14. Create a new column on the mpg dataset named
# #  is_automatic that holds boolean values denoting
# #  whether the car has an automatic transmission.
print('\nExercises II, Question 14')
mpg.trans.value_counts()
mpg.trans.str.contains('auto')
mpg['is_automatic'] = mpg.trans.str.contains('auto')
print(mpg.head())


# # 15. Using the mpg dataset, find out which which
# #  manufacturer has the best miles per gallon on average?
print('\nExercises II, Question 15')
# Any of the below will work for question 15
mpg.groupby('manufacturer').mean().average_mileage.sort_values().tail(1)
mpg.groupby('manufacturer').mean().average_mileage.sort_values(ascending=False).head(1)
mpg.groupby('manufacturer')['average_mileage'].mean().nlargest(1)
mpg.groupby('manufacturer').mean().average_mileage.nlargest(1)

# # 16. Do automatic or manual cars have better miles per gallon?
print('\nExercises II, Question 16')
mpg.groupby('is_automatic').mean().average_mileage.head(1)


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
pd.read_sql(url) # This will allow you to see how many tables are in the database. 
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


# ************** Option 3 **************
order_price = orders_table_df.groupby('order_id').item_price.sum()

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

# ************** Option 3 **************
popular_three_items = orders_table_df.groupby('item_name').quantity.sum().sort_values(ascending=False).head()
print(f'\n************** Option 3 **************\n',popular_three_items)


# 3. Which item has produced the most revenue?
print('\n\nExercises III, Question 3')

# ************** Option 1 **************

# Use the pivot_table() method to group orders by item_name and order_id
#  and sum the quantity and item_price columns for each group
order_totals = pd.pivot_table(orders_table_df, index='item_name',\
                               values=['quantity', 'item_price'], aggfunc=np.sum)


# Created another column named "total_price" by multipling the quantity and item price
order_totals['total_price'] = order_totals['quantity'] * order_totals['item_price']


# Use the nlargest() method to return the row with the highest total item_price
most_revenue = order_totals.nlargest(1, 'total_price')

print(f'The item with the most Revenue\n\n',most_revenue)

# ************** Option 2 **************

orders_table_df[orders_table_df.item_name == 'Chicken Bowl'].sort_values('quantity')

most_revenue_opt2 = orders_table_df.groupby('item_name').item_price.sum().nlargest(1)
print(f'The item with the most Revenue - Option 2\n\n',most_revenue_opt2)


# 4. Join the employees and titles DataFrames together.
print('\nExercises III, Question 4')
url = get_db_url('employees') # Employees is the database were the orders table is coming from.
# Don't forget that Employee is a database not a table.
titles_table_df = pd.read_sql('SELECT * FROM titles', url) # Title is a table. The table is located in the mySQL and was limited to 1000 rows
employees_table_df = pd.read_sql('SELECT * FROM employees', url) # Employees is a table. The table is located in the mySQLL and was limited to 1000 rows
print('\n',titles_table_df.head())

print('\n',employees_table_df.head())

# format: pd.merge(df1,df2, how='', on='column_name') 
# The how is asking if you want to do it by 'inner', 'outer', 'left', or 'right'.
# The on= can only be used if both tables have the same name (emp_no) in the columns if they have
#  differen names use the left_on='emp_num' and right_on='employee_number'. All this is assuming that the 
# values inside the columns are the same. 
# the "how='emp_no'" doesn't have to be listed because is a default. 
et_tt_merge_df = pd.merge(titles_table_df, employees_table_df, how='inner', on='emp_no')
print('\n',et_tt_merge_df)


et_tt_merge_df

et_tt_merge_df.describe(include='all')


# 5. For each title, find the hire date of the employee
# that was hired most recently with that title.
print('\nExercises III, Question 5')

# Examples of sorting and groupby
    # df.sort_values(by='col1', ascending=False)
    # format: df.groupby('column_name').agg_function()
    # df.groupby('room').max()[['math','reading','english']]

# This will give you the olddest date. 
# Utilizied .max() as assending
et_tt_merge_df.groupby('title').hire_date.min() 

# This will give you the most current date. 
# Utilizied .max() as dessending
recently_hire = et_tt_merge_df.groupby('title').hire_date.max()

print(f'The employees that were hired most recently by title: \n\n',recently_hire)

max_hire_dates = et_tt_merge_df.groupby('title').hire_date.max()
max_hire_dates = pd.DataFrame(max_hire_dates).reset_index()
max_hire_dates

pd.merge(et_tt_merge_df, max_hire_dates, on=['title', 'hire_date']).sort_values('title')

# 6. Write the code necessary to create a cross tabulation
# of the number of titles by department. (Hint: this 
# will involve a combination of SQL code to pull the 
# necessary data and python/pandas code to perform the
# manipulations.)
print('\nExercises III, Question 6')
url = get_db_url('employees')

et_tt_merge_df

# Join the department employee and the department using department number with MySQL 
emp_dept = pd.read_sql('''
select *
from dept_emp
    join departments
        using(dept_no)
''', url)

# Display the head of the employee department table
emp_dept.head()

# Display the head of the merge of the employee and title table
et_tt_merge_df.head()

# Merge the employees/title table with the employees department using the employee number
et_tt_dt_df = pd.merge(et_tt_merge_df, emp_dept, on='emp_no')
et_tt_dt_df.head()

# Utilize the crosstab to show both tables
pd.crosstab(et_tt_dt_df.title, et_tt_dt_df.dept_name)

