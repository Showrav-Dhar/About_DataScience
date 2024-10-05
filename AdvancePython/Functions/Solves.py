# Problem: Write a function to calculate and return the square of a number.
#
# def calSquare(a):
#     return a * a
#
#
# user_input = int(input("Enter a number - "))
# print("The square of the number is ", calSquare(user_input))

# Problem: Create a function that takes two numbers as parameters and returns their sum.

# def calsum(a,b,c):
#     return a+b+c
#
# user_input1 = int(input("Enter a number - "))
# user_input2 = int(input("Enter another number - "))
# user_input3 = int(input("Enter last number - "))
# print("The sum of 3 numbers is = ",calsum(user_input1,user_input2,user_input3))

# Polymorphism in function means that a function will act different in different scenarios
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.
# def multi(a, b):
#     return a * b
#
#
# # two numbers
# print("Multiplication of two numbers = ", multi(10, 4))
# print("Multiplication of two strings = ", multi("DIP", 5))


# Problem: Create a function that returns both the area and circumference of a circle given its radius.

# import math
#
#
# def cal(radius):
#     area = math.pi * (radius * radius)
#     circum = 2 * math.pi * radius
#
#     return area, circum
#
#
# radius = int(input("Enter Radius of the circle - "))
# a, b = cal(radius)
# print(f"Area = {round(a, 3)}, circumference = {round(b, 3)}")

# Default Parameter Value
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

# def greet(user_name="user"):
#     return "Hello " + user_name + " Good Morning!"
#
#
# if __name__ == '__main__':
#     print(greet())
#     user_name = input("Enter username - ")
#     print(greet(user_name))


# lambda functions
# lambda argument(s) : expression
# to use lambda function we don't need to use - def keyword

# greet = lambda : print("Testing lambda function")
# greet
# lambda that accepts one argument
# greet_user = lambda user_name : print(f"Hey there {user_name}")
#
# #call
# greet_user("Showrav")

# Problem: Create a lambda function to compute the cube of a number.

# cube_cal = lambda number: number ** 3
#
# user_input = int(input("Enter a number to calculate the cube of it - "))
# print(cube_cal(user_input))


# Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

# def cal_sum(*args):
#     print(args)
#     for i in args:
#         print(i * 2)
#
#     print("Sum = ", sum(args))
#
#
# if __name__ == '__main__':
#     cal_sum(1, 2, 3, 4)

# Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

# def intro(**data):
#     print(type(data))
#     for key, value in data.items():
#         print(f"{key} = {value}")
#
# if __name__ == '__main__':
#     intro(Usar_name = "Showrav", age = 24, gender = "M", Location = "Chittagong")
#     intro(Usar_name="Showrav", age=24, gender="M", Location="Chittagong")
#     intro(Usar_name="Showrav", age=24, gender="M", Location="Chittagong",Mail = "random@gmail.com")
#
# Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit

# Python Generator function

# def my_gen(limit):
#     for i in range(2, limit + 1, 2):
#         yield i
#
#
# if __name__ == '__main__':
#     limit = int(input("Enter a number - "))
#     for num in my_gen(limit):
#         print(num)

# Genrator expression

# li = [1,2,3,4,5]
# cube_gen = (i ** 3 for i in li) # cube_gen has the cube of all the numbers of the list
#
# for val in cube_gen:
#     print(val)

# Pipelining Generators
# def magic_num(nums):
#     x = 0
#     y = 1
#     for _ in range(nums):
#         x, y = y, x * 3
#         yield x
#
#
# def cube_gen(nums):
#     for num in nums:
#         yield num ** 3
#
#
# if __name__ == '__main__':
#     ## Cube sum of magic numbers
#     print(sum(cube_gen(magic_num(10))))
#     # first magic_num will create magic 10 magic numbers
#     # then the cube of them will be calculated
#     # then the sum of them will be calculated

# Problem: Create a recursive function to calculate the factorial of a number.

def fact(num):
    if num == 1:
        return num
    return fact(num - 1) * num

if __name__ == '__main__':
    print(fact(5))








