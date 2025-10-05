# Exercise 1: Sum of Squares
""" Write a Python program that calculates and prints the sum of the squares of numbers from 1 to 5 using a
for loop. """

# total = 0 
# for i in range(1,6):
#     result = i ** 2
#     print(f'square of {i} is {result}')
#     total += result
# print(f'sum of the squares of numbers from 1 to 5 is {total}')

#Exercise 2: Countdown
""" Write a Python program that uses a while loop to print a countdown from 5 to 1."""
# i = 5
# while i>= 0:
#     print(f'count down: {i}')
#     i-=1 # i = i-1
#Exercise 3: 
""" Multiplication Table with Nested For Loop
Write a Python program to print the multiplication table for a user-specified number using 
a nested for loop."""

# num = int(input("Enter the number: "))
# for i in range(1,11):
#     print(f'{num} X {i} = {num*i}')

# ----------------------------------------------
num = int(input("Enter the number: "))
for i in range(1,2):
    print(f'Mutiplication table of {num}')
    for j in range(1,2):
        print(f'{num} X {j} = {num*j}')
        