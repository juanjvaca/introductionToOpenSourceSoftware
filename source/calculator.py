''' This program is a simple terminal calculator that can add, subtract, multiply and divide using functions '''

# define functions
def add(x, y):
   """This  adds two numbers"""
   return x + y

def subtract(x, y):
   """This  subtracts two numbers"""
   return x - y

def multiply(x, y):
   """This multiplies two numbers"""
   return x * y

def divide(x, y):
   """This divides two numbers"""
   return x / y

# this takes the input from the user
print("Select a function.")
print("1.Add + ")
print("2.Subtract - ")
print("3.Multiply * ")
print("4.Divide / ")

choice = input("Pick either 1, 2, 3, or 4:")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Uh oh, can't do that :( ")