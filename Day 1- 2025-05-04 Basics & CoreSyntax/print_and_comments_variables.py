#  For Print the text in the console 

# print
print("I am learning Python Language")
# This is a comment in python

import sys

print(sys.version)
# Python Indentation
if 5 > 2:
# print("Five is greater than two!")  # This will raise an error because there is no indentation
  print("Five is greater than two!")  # This will NOT raise an error because there is indentation


# Variables

x = "awesome" # This is a string variable
print("Python is " + x) # This will print "Python is awesome"

x = "Python is " # This is a string variable with a space at the end. Above same variable x will be overwritten by this line.
y = "awesome"   # This is a string variable
z =  x + y  # This will print "Python is awesome" using + operator between variable x and y to concatenate strings.
print(z) # This will print "Python is awesome"

s = 10 # This is an integer variable
t = 5 # This is an integer variable
# arithmetic operators + - * / // % **
print(s + t) # This will print 15 because s = 10 and t = 5 and 10 + 5 = 15
print(s - t) # This will print 5 because s = 10 and t = 5 and 10 - 5 = 5
print(s * t) # This will print 50 because s = 10 and t = 5 and 10 * 5 = 50
print(s / t) # This will print 2.0 because s = 10 and t = 5 and 10 / 5 = 2.0
print(s // t) # This will print 2 because s = 10 and t = 5 and 10 // 5 = 2 and this is called floor division
print(s % t) # This will print 0 because s = 10 and t = 5 and 10 % 5 = 0 and this is called modulus
print(s ** t) # This will print 100000 because s = 10 and t = 5 and 10 ** 5 = 100000 and this is called exponent operator(power)


myvar = "Python is powerful language"
my_var = "Python is powerful language"
_my_var = "Python is powerful language"
myVar = "Python is powerful language"
MYVAR = "Python is powerful language"
myvar2 = "Python is powerful language"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)


#camelCase
myVariableName = "camelCase"
print(myVariableName)

#PascalCase
MyVariableName = "PascalCase"
print(MyVariableName)

#snake_case
my_variable_name = "snake_case"
print(my_variable_name)

#Many Values to Multiple Variables

x, y, z = "Tesla", "BYD", "Tata"
print(x)
print(y)
print(z)


#One Value to Multiple Variables

x = y = z = "Tesla"
print(x)
print(y)
print(z)

#Unpack a Collection

fruits = ["sagar", "sagar1", "sagar2"]
x, y, z = fruits
print(x)
print(y)
print(z)


#multiple comments
"""
This is a comment
written in
more than just one line
"""


#global variable
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


y = "wow" # This is a global variable

def myfunc():
    
  y = "great" # This is a local variable
  print("Python is " + y)

myfunc()

print("Python is " + y)