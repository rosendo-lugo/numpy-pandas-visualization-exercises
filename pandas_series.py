import pandas as pd
import numpy as np
from pydataset import data



fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]


type([fruits])

fruits[0]

pd.Series(fruits)
fruits_series = pd.Series(fruits)
type(fruits_series)
# # # # fruits_series

# fruits_series.head()

type(fruits_series)

fruits_series

# 1. Determine the number of elements in fruits.
type(fruits_series)
fruits_series.size
fruits_series.count()
        # 17


# 2. Output only the index from fruits.
fruits_series.index
    # RangeIndex(start=0, stop=17, step=1)

# 3. Output only the values from fruits.
fruits_series.values
    # array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
    #    'honeycrisp apple', 'tomato', 'watermelon', 'honeydew', 'kiwi',
    #    'kiwi', 'kiwi', 'mango', 'blueberry', 'blackberry', 'gooseberry',
    #    'papaya'], dtype=object)


# 4. Confirm the data type of the values in fruits.
fruits_series.dtype
    # dtype('O')

# 5. Output only the first five values from fruits.
fruits_series.head()
    # 0         kiwi
    # 1         mango
    # 2    strawberry
    # 3     pineapple
    # 4    gala apple


# 5a. Output the last three values. 
fruits_series.tail(3)
    # 14    blackberry
    # 15    gooseberry
    # 16        papaya  
       
# #5b. Output two random values from fruits.
fruits_series.sample(2)
    # 15    gooseberry 
    # 8     honeydew


# 6. Run the .describe() on fruits to see what information it 
# returns when called on a Series with string values.
fruits_series.describe()
    # count       17
    # unique      13
    # top       kiwi
    # freq         4
    # dtype: object

# 7. Run the code necessary to produce only the unique string values from fruits.
for i in fruits_series.unique():
    print(i)
    # kiwi
    # mango
    # strawberry
    # pineapple
    # gala apple
    # honeycrisp apple
    # tomato
    # watermelon
    # honeydew
    # blueberry
    # blackberry
    # gooseberry
    # papaya

type(i)
    # str

# 8. Determine how many times each unique string value occurs in fruits.
# for i in fruits_series.unique():
#     print(i.count(0))

fruits_series.value_counts()
    # kiwi                4
    # mango               2
    # strawberry          1
    # pineapple           1
    # gala apple          1
    # honeycrisp apple    1
    # tomato              1
    # watermelon          1
    # honeydew            1
    # blueberry           1
    # blackberry          1
    # gooseberry          1
    # papaya              1
    # dtype: int64


# 9. Determine the string value that occurs "most" frequently in fruits.
fruits_series.mode()

# 0    kiwi
# dtype: object


# 10. Determine the string value that occurs "least" frequently in fruits.
print(fruits_series.value_counts().nsmallest(keep='all'))
# unique, counts = np.unique(fruits_series, return_counts=True)
# print(np.asarray((unique, counts)).T)

# b = np.unique(fruits_series, return_counts=True)
# c = b[0][np.argmin(b[1], axis=0)]

# # print(c)
# # print('hi')
# cnt = np.bincount(fruits_series)
# np.nonzero(cnt==cnt[np.nonzero(cnt)].min())[0][0]
