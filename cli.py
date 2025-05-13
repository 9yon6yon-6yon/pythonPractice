# creating command line interfaces (CLI) e.g. app.py arg1 arg2

'''argumented cli'''

# import argparse

# my_parser = argparse.ArgumentParser(prog="app")

# my_parser.add_argument('Argument1', help='This is dummy argument')
# my_parser.add_argument('Argument2', help='This is dummy argument')


# args = my_parser.parse_args()
# print("Done executing")

'''application that does arithmetic calculations'''
# import argparse

# my_parser = argparse.ArgumentParser(prog="Calculating app", description="App that does addition, substraction, multiplication, division")

# my_parser.add_argument('arg1', help='The first entry', type=int)
# my_parser.add_argument('arg2', help='This second entry',type=int)

# args = my_parser.parse_args()

# # a = int(args.arg1)
# # b = int(args.arg2)

# a = args.arg1
# b = args.arg2

# print("The Summation is         : ", a+b)
# print("The Subtraction is       : ", a-b)
# print("The Multiplication is    : ", a*b)
# print("The Division is          : ", a/b)

'''reading arguments from an external file'''

# import argparse
# my_parser = argparse.ArgumentParser(prog="Calculating app", fromfile_prefix_chars='@', description="App that does addition, substraction, multiplication, division")

# my_parser.add_argument('arg1', help='The first entry', type=int)
# my_parser.add_argument('arg2', help='This second entry', type=int)

# args = my_parser.parse_args()

# a = args.arg1
# b = args.arg2

# print("The Summation is         : ", a+b)
# print("The Subtraction is       : ", a-b)
# print("The Multiplication is    : ", a*b)
# print("The Division is          : ", a/b)

'''optional arguments'''
import argparse
my_parser = argparse.ArgumentParser(prog="Calculating app", fromfile_prefix_chars='@', description="App that does addition, substraction, multiplication, division")

my_parser.add_argument('arg1', help='The first entry', type=int)
my_parser.add_argument('arg2', help='This second entry', type=int)
my_parser.add_argument('--shift', help='Shift optional argument', type=int)

args = my_parser.parse_args()

a = args.arg1
b = args.arg2
shift = args.shift

if shift == None:
    shift = 0
else:
    shift = shift

print("The Summation is         : ", a+b+shift)
print("The Subtraction is       : ", a-b+shift)
print("The Multiplication is    : ", a*b+shift)
print("The Division is          : ", a/b+shift)