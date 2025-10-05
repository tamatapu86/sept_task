#syntax
# def functionname():
#     #function block of code

# def add():
#     num_1 = 10
#     num_2 = 20
#     num_3 = 30
#     print(num_1+num_2+num_3)
#     print("welcome to pythonlife")
# add()


# def greet(): #function definition
#     print("hello everyone") #function body
#     age = 35 #function body
#     print(age+50) #function
# greet() #function calling
# greet() #function calling
# greet() #function calling
# greet() #function calling



# def sample():#function definition
#     for i in range(11):#function body
#         print(i)
# sample()#function calling



# def details(name,id):#function definition
#     print(name)#function body
#     print(id)#function body
# details("srikar",1234)#function calling , here srikar and 1234 are the arguments(values)
# details("vasi",2345)
# details("prasad",5234)



# def add(num_1,num_2,num_3):#function definition
#     print(num_1+num_2+num_3)#function body
# add(25,25,50)
# def sample(a):
#     print(a)
# sample(["srikar","vasu","pythonlife",5.7,25,True])


#arbitary arguments--> function can accept a variable number of arguments by using *args(syntax)
# def sample(*a):
#     print(a)
# sample("srikar","vasu","pythonlife",5.7,25,True)

# * --> all


# a = 25,35,5.7,"pythonlife"



#keyword arguments :-->keyword arguments are passed to a function with a keyword and a value, allowing for more explicit parameter passing

#**
# def sample(**a):
#     print(a)
# sample(a=5,b=10,c=20)


# * --> tuple
# ** --> dict


# def details(user=None,dept="frontend",id=None):
#     print(user,dept,id)
# details("vasu","fullstack",1234)
# details("raju","front-end",)
# details("srikar",)
# details()





# def discount(price,discount=10):
#     discount_amount = (price * discount )/100
#     final_price = price - discount_amount
#     print(final_price)
# discount(10000,)
# discount(5000,)
# discount(20000,20)



# def add(num1,num2):
#     return num1+num2
# obj = add(50,50)
# print(obj*25)


# def add(num1,num2):
#     return num1+num2
# print(add(50,50))
# print(add(500,50))
# print(add(500,50))
# print(add(50000,50))
# print(add(50,5584980))


#variables ---> two types -->local variables ---> global variables
#1. local variables --> funtion (inside the function )
#2. global variables --> outside the function 


# def details():
#     user = "bharat" #local variables
#     id = 3452 #local variables
#     salary = 100000 #local variables
#     print(user)
#     print(id)
#     print(salary)
#     salary += 50000
#     print(salary)
# details()



# balance = 1000 #global variable
# def credit(amount):
#     global balance
#     user = "srikar"
#     print(user)
#     print(f"credited amount {amount}")
#     balance+=amount
#     print(f"total balance {balance}")


# credit(50000)



# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def expo(a,b):
#     print(a**b)



# pie = 3.14


# add(5,25)
# sub(25,5)
# expo(4,2)