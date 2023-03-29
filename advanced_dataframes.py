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

# def get_db_url(database_name):
#     return f"mysql+pymysql://{username}:{password}@{hostname}/{database_name}"



# url = f"mysql+pymysql://{username}:{password}@{hostname}/{database_name}"
# print(url)  # Output: mysql+pymysql://myusername:mypassword@localhost/mydatabase
# # from env import hostname, username, password, database_name

# # url = f'mysql+pymysql://{username}:{password}@{hostname}/employees'


from env import user, host, password

def get_db_url(database_name):
    return f"mysql+pymysql://{user}:{password}@{host}/{database_name}"

url = get_db_url('employees')

pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url) 




# # 4. Use your function to obtain a connection to the employees database.
# print('\nExercises I, Question 4')


# # 5. Once you have successfully run a query:
# print('\nExercises I, Question 5')


# # 5a. Intentionally make a typo in the database url. 
# print('\nExercises I, Question 5a')


# #   What kind of error message do you see?

# # 5b. Intentionally make an error in your SQL query.
# print('\nExercises I, Question 5b')


# #   What does the error message look like?

# # 6. Read the employees and titles tables into two separate DataFrames.
# print('\nExercises I, Question 6')


# # 7. How many rows and columns do you have in each DataFrame? 
# print('\nExercises I, Question 7')


# #   Is that what you expected?

# # 8. Display the summary statistics for each DataFrame.
# print('\nExercises I, Question 8')


# # 9. How many unique titles are in the titles DataFrame?
# print('\nExercises I, Question 9')


# # 10. What is the oldest date in the to_date column?
# print('\nExercises I, Question 10')


# # 11. What is the most recent date in the to_date column?
# print('\nExercises I, Question 10')