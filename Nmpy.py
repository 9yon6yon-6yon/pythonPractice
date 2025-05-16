from numpy.random import default_rng
import numpy as np
'''regular shape structure'''
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(arr.shape)
# print(arr.dtype)
'''serching for elements'''
# arr = np.array(['john', 'marshmello','jack','alex'])
# index = np.where(arr=='jack')
# # print(index[0])
# print(index[0][0])
'''maxmin in array'''
# arr = np.array([50,20,30,22,24,49])
# maximum = np.amax(arr)
# print(maximum)
# minimum = np.amin(arr)
# print(minimum)
'''sorting an array'''
# arr = np.array([50,20,30,22,24,49])

# sort = np.sort(arr)#asc
# print(sort)

# sort = -np.sort(-arr)#desc
# print(sort)

'''combine/merge two array'''

# a = np.array([30,20,10])
# b = np.array([50,60,70])

# c = np.concatenate([a,b])
# print(c)

'''splitting array'''

# a = np.array([10,20,30,40,50,60,70,80])

# splt = np.hsplit(a,2)
# print(splt)
# print(splt[0])
# print(splt[1][0])

'''random array generator'''

# arr = np.random.default_rng().integers(100, size=(1, 5))#1D array with 5 elements between 0 - 100
# print(arr)
'''reshaping an array'''

arr = np.array([1,2,3,4,5,6])
b = arr.reshape(3,2)
print(b)

