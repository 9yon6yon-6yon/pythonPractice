'''passing function to a function'''


def calcFormula(x, y):
    return x * y + x / 2 + 2


def calcFormula2(x, y):
    return x*x*x+y*y*y


# def printOutputReport(func, x, y):
#     z = func(x, y)
#     print('-----------This is a report for your formula-----------')
#     print('Value for x is : ', x)
#     print('Value for y is : ', y)
#     print('Calculated result for your formula is : ', z)


# printOutputReport(calcFormula, 3, 4)

# printOutputReport(calcFormula2, 5, 6)

def printOutputReport(func):
    def f(x,y):
        z = func(x, y)
        print('-----------This is a report for your formula-----------')
        print('Value for x is : ', x)
        print('Value for y is : ', y)
        print('Calculated result for your formula is : ', z)
    return f
calcFormula2 = printOutputReport(calcFormula2)

calcFormula2( 3, 4)
