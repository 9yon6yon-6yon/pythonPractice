'''to prevent code from crashing.
an error that causes a program to crash
e.g. c = 2/0 which makes an ZeroDivisionError 
'''


# a = 0
# b = 2
# c = b/a
# try:
#     c = b/a
#     print(c)
# except:
#     print('Division is not possible for the given numbers')

'''exception types'''
# named error
# c = b/x ; this is an error for x where x is not defined before
# try:
#     c = b/x
#     print(c)
# except NameError:
#     print('Variable is not defined for x')

'''multiple exceptions'''
# a = 10
# b = 2
# i = 3
# x = 5
# try:
#     c = a/x
# except NameError:
#     c = a/i
#     print('Variable is not defined yet')
# else:
#     x = 100
#     print(x)
# finally:
#     print('This will execute no matter what........')

# try:
#     print('Creating a folder')
# except:
#     print('Folder does exists. Can not create')
# else:
#     print('Put 5 files in that folder')
# finally:
#     print('Folder created successfully')

'''catching the actual exception'''
# a = 0
# b = 2

# try:
#     c = b/a
# except Exception as e:
#     print(e)
'''custom exceptions'''
class CustomException(Exception):
    pass
class ElementDoesNotExist(CustomException):
    pass
class FirstElementIsSmallerThanSecond(CustomException):
    pass

list = [1,2,3,4,5]
try:
    if not 8 in list:
        raise ElementDoesNotExist
except ElementDoesNotExist:
    print('Element Does not exists')
else:
    print('Element Exist')