# Convention is to import the numpy module as np.
# The following exercises would not work without the import
import numpy as np


a = np.array ([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?

neg_nums = a[a<0]
print("\n", neg_nums[neg_nums < 0],"\n")
    # [-2 -1 -6 -7] 

print(len(neg_nums[neg_nums < 0 ]),"\n")
    # 4

# # 2. How many positive numbers are there?

pos_nums = a[a>0]
print("\n",pos_nums[pos_nums > 0],"\n")
    # [ 4 10 12 23  3] 
print(len(pos_nums[pos_nums > 0 ]),"\n")
    # 5

            # how to find even or odd
            # if n & 2 == 0:
            #   return even
            # else:
            #   return odd

# # 3. How many even positive numbers are there?
# pos_nums[pos_nums % 2 == 0]
# pos_num = len(pos_nums[pos_nums % 2 == 0])


# # print("\n", (all_evens) & (a[a > 0]),"\n")
# b = a[a > 0]
# c = a[a % 2 == 0]
# # print([(a)& (c)])
# print(b)
# print(c)

# # 4. If you were to add 3 to each data point, 
# # # ----how many positive numbers would there be?
# print('\na + 3 == {}\n'.format(a + 3))
# # print("\n", a[a+3],"\n")
three = a + 3
three > 0
three[three > 0]
print(three)

# 5. If you squared each number, 
# ---what would the new mean and standard deviation be?
# print('\na array =',a)
# print('old mean: ',a.mean())
# print('old stddev: ',a.std(),'\n')

# b = (a ** 2)
# print('\nb array =',b)
# print('new mean: ',b.mean())
# print('new stddev: ',b.std(),'\n')

num_sq = a ** 2
num_sq.mean()
num_sq.std()


# 6. A common statistical operation on a dataset is centering. 
# --This means to adjust the data such that the mean of the data is 0. 
# --This is done by subtracting the mean from each data point. 
# --Center the data set. See this link for more on centering.

centered = a - a.mean()

centered.mean()



# print('\na array =',a)
# print(a.mean())
# mn = a.mean()
# zeromn = a - mn
# print(zeromn,'\n')

# 7. Calculate the z-score for each data point. 
# Recall that the z-score is given by:

(a - a.mean()/a.std())
centered/a.std()