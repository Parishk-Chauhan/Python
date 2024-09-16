#  Variables : Variables are containers for storing data values.

# declaring a variable 

# python has no command for declaring a variable 

# a variable is cerated the moment it is assigned with a value

age = 21          # this is an int 

name = "Parisk Chauhan"         #this is a str 

# printing the variables : 

print(age)
print(name)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 5   # it is an integer 
print(x)
x = "Gunnu Chauhan"               # x is reassigned to be a str
print(x)

# Casting : If you want to specify the data type of a variable, this can be done with casting.

x = str(1)      #x will be '3'
y = int(3)      #y will be 3
z = float(3)    #z will be 3.0 

# more about int str and float in data types;

# Get the type of variable 

a = 5
b = "John"
print(type(a))
print(type(b))

# Single or Double Quotes?
# String variables can be declared either by using single or double quotes:

last_name = "Chauhan"
first_name = 'Dhia'

print(first_name)
print(last_name)

# case sensitive

p = "Parishk"
# is not same as 
P = "Parishk Chauhan"

# P will not overwrite p 