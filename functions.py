# syntax
# def functionname()
#   #function block of code

# def add():
#     num_1 = 10
#     num_2 = 20
#     num_3 = 30
#     print(num_1+num_2+num_3)
#     print("welcome to pythonlife")
# add()
# ====================================================

# def greet(): #function defenition
#     print("Hello every one")    #function body
#     age = 35 #function body
#     print(age + 50) #function body
# greet() #function calling
# greet() #function calling
# greet() #function calling
# greet() #function calling
# ====================================================


def sample():  #function name
    for i in range(11): #function body
        print(i)    #function body
sample()  #function calling

# ====================================================
#parameters and Arguments
# def details(name , id): #function name
#     print(name)
#     print(id)
# details("mohan",1234)
# details("vasu",2345)
# details("srinu",9875)
# ====================================================

# def sample(*a*):
#     print(a)
# sample(a=5,b=10,c=20)
# ====================================================

# def details(user=None,dept= "Sales",id = None):
#     print(user,dept,id)
# details("vasu","com",1234)
# details("mohan","fin")
# details("krishna")
# details()

# ====================================================
# return statement
# def add(num1,num2):
#     return(num1+num2) # to exit function
# obj = add(50,50)
# print(obj)
# ====================================================


# return statement
# def add(num1,num2):
#     return(num1+num2) # to exit function
# print(add(20,52))

# ====================================================
# local Varaibles and Global Variables

# def details():
#     user = "mohan" #local variables
#     id = 3452 #local variables
#     salary = 100000 #local variables
#     print(user)
#     print(id)
#     print(salary)
# details()


# balance = 1000 #global Variables
# def credit(amount):
#     user = "srikar"
#     print(user)
#     print(balance)
# credit(20000)

#=====================Calculator================================
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
    print(a*b)
def expo(a,b):
    print(a**b)

add(52,67)
sub(25,12)
mul(9,9)
expo(4,2)








