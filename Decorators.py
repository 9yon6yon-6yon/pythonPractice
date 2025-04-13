'''passing function to a function'''



# def printOutputReport(func, x, y):
#     z = func(x, y)
#     print('-----------This is a report for your formula-----------')
#     print('Value for x is : ', x)
#     print('Value for y is : ', y)
#     print('Calculated result for your formula is : ', z)


# printOutputReport(calcFormula, 3, 4)

# printOutputReport(calcFormula2, 5, 6)

def printOutputReport(func):
    def f(*args, **kwargs):
        z = func(*args, **kwargs)
        print('-----------This is a report for your formula-----------')
        for i, ar in enumerate(args):
            print('Your '+ str(i + 1) +' variable is : ', ar)
        print('Calculated result for your formula is : ', z)
    return f
@printOutputReport
def calcFormula(x, y):# now we can just modify the function only not the wrapper function
    return x * y + x / 2 + 2

@printOutputReport
def calcFormula2(x, y):
    return x*x*x+y*y*y

calcFormula2( 3, 4)
