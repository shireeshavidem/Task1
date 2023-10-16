# 1.Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

# string = input("enter your string:  ")
# def count_lower_upper(string):
#     count = {"upper_case":0,"lowe_case":0}
#     for i in string:
#         if i.isupper():
#             count["upper_case"]+=1
#         elif i.islower():
#             count["lowe_case"]+=1
#         else:
#             pass
#     print("No. of Upper case characters: ",count["upper_case"])
#     print("No. of Lower case characters: ",count["lowe_case"])    
# count_lower_upper(string)           

# 2.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

# list = []
# n = int(input("enter no of elements: "))
# new_list = []
# def result_list(list,new_list):
#     for i in range(0,n):
#         list1 = input("Enter list elements: ")
#         list.append(list1)
#     for j in list:
#         if j not in new_list:
#             new_list.append(j)
#     print(list)
#     print(new_list)
# result_list(list,new_list) 

# 3.Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog". 

# string = input("Enter your string: ")
# def ispanagram(string):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for i in alphabet:
#         if i not in string.lower():
#             return False
#         return True
# if (ispanagram(string)==True):
#     print("Yes")
# else:
#     print("No")   


# 4.Write a Python function to create and print a list where the values are the squares of numbers between 1 and 10 (both included). 

# def printSquares():
# 	sqrs = list()
# 	for i in range(1,11):
# 		sqrs.append(i**2)
# 	print(sqrs)
# printSquares()

# 5.Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20 

# n = int(input("enter no of elements: "))
# def sumValue():
#     list = []
#     sum = 0
#     for i in range(0,n):
#         list1 = int(input("Enter list elements: "))
#         list.append(list1)
#     for i in range(len(list)):
#         sum = sum + list[i]
#     print(list)
#     print(sum)    
# sumValue()

# 6.write a function to find sum of given values, pass values has variable number of arguments to function.
def add_num(*args):
   sum = 0
   for num in args:
      sum += num
   return sum
add_num(1, 2, 3)
print(add_num(1, 2, 3))
add_num(10, 20, 30, 40)
print(add_num(10, 20, 30, 40))
add_num(5, 6, 7, 8, 9)
print(add_num(5, 6, 7, 8, 9))
