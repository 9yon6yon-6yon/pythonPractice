# '''normal function'''

# def addToDatabase(name):
#     # print(name)
#     db1 = ['Kate', 'Lee', 'Steve']
#     db2 = ['No', 'Never', 'None']

#     db1.append(name)
#     print(db1)

# addToDatabase("John Doe")
# addToDatabase("Lorem Ipsum")


# '''global variables'''

# globalVar = 'This is a global variable'
# def Function1():
#     global var1
#     var1 = 'This is global from function 1'
# def Function2():
#     var1 = 'This is in Function 2'

'''return functions'''


def pwr2(num):
    pw2 = num*num
    div = num/num
    return pw2, div



pw2 , div = pwr2(5)
print(pw2,div)