# recursion function
# Program to print the fibonacci series upto n_terms

n_terms = int(input("Enter the range: "))

# if n_terms <= 0:
#   print("Invalid input ! Please input a positive value")
# else:
#   print("Fibonacci series: ")
def recursive_fibonacci(n):
  if n <= 1:
       return n
  else:
	  return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
for i in range(n_terms):
	print(recursive_fibonacci(i))


# Program to print factorial of a number
# recursively.

# n = int(input("Enter factorial number: "))
# # Recursive function
# def recursive_factorial(n):
#   if n == 1:
# 	  return n
#   else:
# 	  return n * recursive_factorial(n-1)
# print(recursive_factorial(n))

# # check if the input is valid or not
# if n  < 0:
#   print("Invalid input ! Please enter a positive number.")
# elif n == 0:
#   print("Factorial of number 0 is 1")
# else:
#   print("Factorial of number", n, "=", recursive_factorial(n))

#Program using non-tail recursion
# n = int(input("Enter range: "))
# def Recur_facto(n):
#     if (n == 0):
#         return 1
#     return n * Recur_facto(n-1)
# print(Recur_facto(n))

#program using tail-recursion
# n = int(input("Enter range: "))
# def Recur_facto(n, a = 1):
#     if (n == 0):
#         return a
#     return Recur_facto(n-1, n * a)
# print(Recur_facto(n))


 #map() 
# numbers = (1,2,3,4)
# # Return double of n 
# def addition(n): 
# 	return n + n 
# # We double all numbers using map()  
# result = map(addition, numbers) 
# print(list(result)) 

# Double all numbers using map and lambda 
# numbers = (1, 2, 3, 4) 
# result = map(lambda x: x + x, numbers) 
# print(list(result)) 


# Add two lists using map and lambda 

# numbers1 = [1, 2, 3] 
# numbers2 = [4, 5, 6] 
# result = map(lambda x, y: x + y, numbers1, numbers2) 
# print(list(result)) 


#filter()
# function that filters vowels
# sequence = ['s','h','i', 'r', 'e', 'e', 's', 'h', 'a']
# def fun(variable):
# 	letters = ['a', 'e', 'i', 'o', 'u']
# 	if (variable in letters):
# 		return True
# 	else:
# 		return False
# # sequence
# filtered = filter(fun, sequence)
# print('The filtered letters are:')
# for s in filtered:
# 	print(s)

# Define a function to check 
# if a number is a multiple of 3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_multiple_of_3(num):
	return num % 3 == 0
result = list(filter(lambda x: is_multiple_of_3(x), numbers))
print(result)

# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]
#odd numbers
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))
#even numbers
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))


#reduce

# program working of reduce() 
# importing functools for reduce() 
import functools 
# importing operator for operator functions 
import operator 
# initializing list 
lis = [1, 3, 5, 6, 2] 
# sum of list 
# using operator functions 
print("The sum of the list elements is : ", end="") 
print(functools.reduce(operator.add, lis)) 
#product of lidt elements
# using operator functions 
print("The product of list elements is : ", end="") 
print(functools.reduce(operator.mul, lis)) 
# using reduce to concatenate string 
print("The concatenated product is : ", end="") 
print(functools.reduce(operator.add, ["python", "is", "difficult"])) 

# python code to demonstrate summation 
# using reduce() and accumulate() 
# importing itertools for accumulate() 
import itertools 
import functools 
# initializing list 
lis = [1, 3, 4, 10, 4] 
# printing summation using accumulate() 
print("The summation of list using accumulate is :", end="") 
print(list(itertools.accumulate(lis, lambda x, y: x+y))) 
# printing summation using reduce() 
print("The summation of list using reduce is :", end="") 
print(functools.reduce(lambda x, y: x+y, lis))


# Python program to illustrate sum of two numbers. 
def reduce(function, iterable, initializer=None): 
	it = iter(iterable) 
	if initializer is None: 
		value = next(it) 
	else: 
		value = initializer 
	for element in it: 
		value = function(value, element) 
	return value 
# Note that the initializer, when not None, is used as the first value instead of the first value from iterable , and after the whole iterable. 
tup = (2,1,0,2,2,0,0,2) 
print(reduce(lambda x, y: x+y, tup,6))

#lambda function
format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"
print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))
def cube(y):
	return y*y*y

lambda_cube = lambda y: y*y*y

# using function defined
# using def keyword
print("Using function defined with `def` keyword, cube:", cube(5))
# using the lambda function
print("Using lambda function, cube:", lambda_cube(5))


is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
	print(item())

#Nested function
#1
def f1(): 
	s = 'Me too'
	def f2():
		s = 'I love python'
		print(s) 
	f2()
	print(s) 
f1() 

#2
def f1(): 
    s = ['I love python']  
    def f2(): 
        s[0] = 'Me too'
        print(s)       
    f2() 
    print(s)
f1()

#3
def f1(): 
	f1.s = 'I love python'
	def f2(): 
		f1.s = 'Me too'
		print(f1.s) 
	f2() 
	print(f1.s) 
f1() 
