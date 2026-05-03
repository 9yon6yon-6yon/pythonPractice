
def Factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * Factorial(num - 1)

while(True):
    number = int(input("Enter a number: "))
    print(Factorial(number))