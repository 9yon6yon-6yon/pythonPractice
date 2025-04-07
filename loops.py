# while(1):
#     userInput = input('Enter a letter: ')
#     if userInput == 'Q':
#         break
#     print(userInput)

'''for loops'''
# for i in range(1, 101, 2):
#     print(i)
# l = ['apples', 'bananas', 'strawberries']
# for i in l:
#     print(i)

# '''enumeration'''

# cars = ['BMW', 'Hyundai', 'Honda', 'Toyota']

# for i, items in enumerate(cars):
#     print(i, items)

# '''zip'''

# shapes = ['square', 'circle', 'Triangle']
# centers = [(10, 10), (50, 50), (100, 100)]

# # for i in range(0, len(shapes)):
# #     print(shapes[i], centers[i])
# for shape, center in zip(shapes, centers):
#     print(shape, center)

'''list comprehension'''
S = "This is a string"

Li = [ x for x in S if x!=' ' and x!='i' ]
print(Li)
