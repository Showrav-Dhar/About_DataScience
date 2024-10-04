from math import sqrt

# problem 1
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# ct = 0
# # for i in range(0, len(numbers)):
# #     if numbers[i] >= 0:
# #         ct += 1
# #
# # print(ct)
#
# # for num in numbers:
# #     if num > 0:
# #         ct+=1
# #
# # print(ct)

# Problem: Calculate the sum of even numbers up to a given number n.

# n = int(input("Enter a number - "))
# # print(n)
# sum = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         # print(i)
#         sum += i
#
# print(sum)

# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

# for i in range(1,10+1):
#     if i == 5:
#         continue
#     print(str(10)+" * "+str(i)+" = "+str(10*i))

# Problem: Reverse a string using a loop.

# input_string = input("Enter a string = ")
# reversed_string = ""
#
# for char in input_string:
#     reversed_string = char + reversed_string
#
# print(reversed_string)

# Problem: Given a string, find the first non-repeated character.

# using dictionary
# input_string = "REVERSED"
# freq = {}
#
# for char in input_string:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
#
# for key in freq:
#     val = freq[key]
#     if val == 1:
#         print("the first non-repeated character is = "+key)
#         break

# using built in count method

# input_string = "REVERSED"
#
# for char in input_string:
#     if input_string.count(char) == 1: # checking how many times char is present in input_string
#         print("the first non-repeated character is = "+char)
#         break

# Problem: Compute the factorial of a number using a while loop.

# input_number = int(input("Enter a number = "))
# fact = 1
#
# while input_number !=0 :
#     fact = fact * input_number
#     input_number -= 1
#
# print(f"Factorial of {input_number} is = {fact}")

# Problem: Keep asking the user for input until they enter a number between 1 and 10.
#
# while 1:
#     number = int(input("Enter a number between 1 to 10 - "))
#     if 1 <= number <= 10:
#         print("Validation completed")
#         break
#     else:
#       print("Invalid input")

# Problem: Check if a number is prime.

# num = int(input("Enter a number - "))
# sq = int(sqrt(num))
# fl = 1
# for i in range(2, sq+1):
#     if num % i == 0:
#         print("Number is not prime")
#         fl = 0
#         break
#
# if fl:
#     print("Number is prime")

# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

# items = ["apple", "banana", "orange", "apple", "mango"]

# using count function
# for item in items:
#     ct = items.count(item)
#     if ct > 1:
#         print(item)
#         break

# using set
#
# unique_set = set()
#
# for item in items:
#     if item in unique_set:
#         print("Duplicat = ", item)
#         break
#     else:
#         unique_set.add(item)

# Problem: Implement an exponential backoff strategy that doubles the wait time between retries,
# starting from 1 second, but stops after 5 retries.


