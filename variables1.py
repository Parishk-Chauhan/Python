# Variable Names : 

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.


# some of the legal variable names : 

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variable names : 
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Variable names are case sensitive : 

# Multi Words Variable Names : 

# There are several techniques you can use to make them more readable:

# 1. Camel Case : Each word, except the first, starts with a capital letter:

myVariableName = "John"

# 2. Pascal Case : Each word starts with a capital letter:

MyVariableName = "John"

# 3. Snake Case : Each word is separated by an underscore character:

my_variable_name = "John"


# Many Values to Multiple Variables

x, y, z = "Banana", "Car", "Bike"

print(x)
print(y)
print(z)

# Note: Make sure the number of variables matches the number of values, or else you will get an error.

# One Value to Multiple Variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

print (x,y,z)

# You can also use the + operator to output multiple variables:

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
print (x,y,z)

# Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

# For numbers, the + character works as a mathematical operator:

x = 4
y = 6

print(x+y)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

x = 5
y = "John"
# print(x + y)             this will give error 

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:


print(x, y)