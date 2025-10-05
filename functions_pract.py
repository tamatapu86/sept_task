#def function_name():
    #function block of code

# def add():
#     num1 = 10
#     num2 = 20
#     num3 = 30
#     print(num1+num2+num3)
#     print("welcome to pythonlife")
# add()

# def greet(): #function definition
#     print("hello everyone") #function body
#     age = 35  #function body
#     print(age + 50) #function body
# greet() #function calling
# greet() #function calling
# greet() #function calling
# greet() #function calling
# greet() #function calling


# def sample():
#     for i in range(11):
#         print(i)
# sample()

#parameters and arguments

# def details(name, id): #function definition
#     print(name)
#     print(id)
# details("mohan",1234) # mohan and 1234 are arguments(values)
# details("VASU",4563) 

# def add(num1,num2,num3):
#     print(num1+num2+num3)
# add(25,25,50)

#arbitary arguments
# def sample(*a):
#     print(a)
# sample("mohan","vasu","mohan",123,3.5,True)

#key arguments
# def sample(**a):
#     print(a)
# sample(a=3,b=6,c=8)

# default parameteres

# def details(user=None,dept="AI",id=None):
#     print(user,dept,id)
# details("Mohan","AI",1234)
# details("Krishna","python",9934)
# details("Sampath","GenAI",)
# details("Raju")
# details()

# return : 

# def add(num1,num2):
#     return num1+num2
# obj = add(50,50)
# print(obj*25)

# def add(num1,num2):
#     return num1+num2
# print(add(50,50))

#local and global variables
#local variables => function (inside the function)
#global variables => outside the function

# def details():
#     user = "mohan" # local variables
#     id = 3452 # local variables
#     salary = 10000 # local variables
#     print(user) # local variables
#     print(id)  # local variables
#     print(salary)  # local variables
# details()


# balance = 1000 #global variables
# def credit(amount):
#     global balance
#     user = "mohan"
#     print(user)
#     print(f'crdited amount {amount}')
#     balance+=amount
#     print(f'total balance {balance}')
# credit(50000)

#module

# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def expo(a,b):
#     print(a**b)
# add(5,25)
# sub(25,5)
# mul(3,64)
# expo(2,2)

# pie = 3.12


# pre defined modules ===> math

# import math
# print(math.sqrt(16))
# print(math.pi)

# from math import *
# print(sqrt(16))
# print(pi)

#random module

# import random
# print(random.randint(1, 10)) # Random integer between 1 and 10
# print(random.choice(['apple', 'banana', 'orange'])) # Randoml

# date and time module

# from datetime import datetime
# now = datetime.now()
# print(now)

# import os
# print(os.getcwd())


# def credit():
#     pass
# def withdraw():
#     pass
















