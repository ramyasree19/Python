name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")
print(f"Hello {name}! Welcome!")

#entered by the user into separate variables for each value using the split() method.
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

#Note: The split() method always returns input values as strings. If you need them as numbers (int or float), you must convert them using typecasting.

#By default input() function helps in taking user input as string. If any user wants to take input as int or float, we just need to typecast it.
n = int(input("How many roses?: "))
print(n)
print(type(n))

#Unlike Java and many other languages, Python variables do not require explicit declaration of type.
#The type of the variable is inferred based on the value assigned.

"""
Rules for Naming Variables
To use variables effectively, we must follow Python’s naming rules:
Variable names can only contain letters, digits and underscores (_).
A variable name cannot start with a digit.
Variable names are case-sensitive like myVar and myvar are different.
Avoid using Python keywords like if, else, for as variable names.

"""
#INVALID VARIABLE NAMES
#1name = "Error"  # Starts with a digit
#class = 10       # 'class' is a reserved keyword
#user-name = "Doe"  # Contains a hyphen

#Multiple assignments
a, b, c = 5, 10.5, "Hello"
print(a)
print(b)
print(c)

x = 10
del x # Deletes the variable x
print(x)