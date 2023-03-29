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

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # 11. How many different models are there?
print('\nExercises II, Question 11')
print(f'\nmodels\n',mpg.model.unique())
print(f'\nDescribe all\n',mpg.describe(include='all'))

# # 12. Create a column named mileage_difference 
# # like you did in the DataFrames exercises; 
# # this column should contain the difference between
# #  highway and city mileage for each car.
print('\nExercises II, Question 12')
# print(mpg['milage_difference'] = mpg.highway - mpg.cty)


# # 13. Create a column named average_mileage like 
# # you did in the DataFrames exercises; this is the 
# # mean of the city and highway mileage.
print('\nExercises II, Question 13')
mpg[['cty','highway']].agg('mean')
print(mpg[['cty','highway']].agg('mean', axis=1))
# print(mpg['average_mileage'] = mpg[['cty','highway']].agg('mean', axis=1))


# # 14. Create a new column on the mpg dataset named
# #  is_automatic that holds boolean values denoting
# #  whether the car has an automatic transmission.
print('\nExercises II, Question 14')
print(mpg.trans.value_counts())
print(mpg.trans.str.contains('auto'))
# print(mpg['auto'] = mpg.trans.str.contains('auto'))

'auto' in mpg.trans
mpg.trans.apply(lambda x: 'auto' in x)
# # 15. Using the mpg dataset, find out which which
# #  manufacturer has the best miles per gallon on average?
print('\nExercises II, Question 15')
print(mpg.groupby('manufacturer').mean().average_mileage.sort_values().tail(1))
print(mpg.groupby('manufacturer').mean().average_mileage.sort_values(ascending=False).head(1))
print(mpg.groupby('manufacturer').mean().average_mileage.nlargest(1))
print(mpg.groupby('manufacturer')('average_mileage').mean().nlargest(1))

# # 16. Do automatic or manual cars have better miles per gallon?
print('\nExercises II, Question 16')
print(mpg.groupby('is_automatic').mean().average_mileage.head(1))