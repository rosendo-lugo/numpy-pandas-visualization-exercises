# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercises III
# Use your get_db_url function to help you 
# explore the data from the chipotle database.
from pydataset import data
import pandas as pd
import numpy as np
import env

# SELECT * FROM chipotle.orders;

url = get_db_url('employees')
test_employees_table = pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url) 
print('\n',test_employees_table)


chipotle_database = pd.read_sql('use chipltle', url) 
print('\n',chipotle_database)


# 1. What is the total price for each order?
print('\nExercises III, Question 1')


# 2. What are the most popular 3 items?
print('\nExercises III, Question 2')


# 3. Which item has produced the most revenue?
print('\nExercises III, Question 3')


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





