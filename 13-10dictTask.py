# 1.Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# dictnry = {}
# add_dict = {}
# for i in range(4):
#     dictkeys = input("Enter your dictinary keys: ")
#     dictvalues = input("Enter your dictionary values: ")
#     dictnry[dictkeys] = dictvalues
# print(dictnry)
# K = input("Enter the key where you want to insert key: ")
# add_key = input("enter key: ")
# add_value = input("enter value: ")
# add_dict[add_key] = add_value
# new_dict = dict()
# for key in dictnry:
#     new_dict[key] = dictnry[key]
#     if key==K:
#         new_dict.update(add_dict)
# print(new_dict)        


#2.Write a Python script to check whether a given key already exists in a dictionary.
# dictionary = {}
# for i in range(4):
#     dictkeys = input("Enter your dictinary keys: ")
#     dictvalues = input("Enter your dictionary values: ")
#     dictionary[dictkeys] = dictvalues
# print(dictionary)
# key = input("Enter key you want to check: ")
# if key == dictkeys:
#     print("key already exists in a dictionary")
# else:
#     print("key doesn't exists in a dictionary")
# print(dictionary)  

#3.Write a Python program to iterate over dictionaries using for loops
# dictionary = {}
# for i in range(4):
#     dictkeys = input("Enter your dictinary keys: ")
#     dictvalues = input("Enter your dictionary values: ")
#     dictionary[dictkeys] = dictvalues
# print(dictionary)
# for key, value in dictionary.items():
#     print(key, ":", value)

# 4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}  
# dictionary = {}
# for keys in range(1,16):
#     values = keys**2
#     dictionary[keys]=values
# print(dictionary)

# 5.Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'marolix technology'
# Expected output: {'m': 1, 'a': 1, 'o': 3, 'l': 2, 'i': 1, 'x': 1, 't': 1, 'e': 1,'c': 1, 'h': 1, 'n': 1, 'g': 1,'y':1}
# dictionary = {}
# string = input("Enter string: ")
# def create_dictionary(string):
#   for letter in string:
#     if letter in dictionary:
#       dictionary[letter] += 1
#     else:
#       dictionary[letter] = 1
#   return dictionary
# create_dictionary(string)
# print(dictionary)

# 6. Write a Python program to sum all the items in a dictionary.
dictionary = {}
n = int(input("Enter range of dictionary: "))
def sum_dict(dictionary):
  for i in range(n):
    dictkeys = int(input("Enter your dictinary keys: "))
    dictvalues = int(input("Enter your dictionary values: "))
    dictionary[dictkeys] = dictvalues
  print(dictionary)
  for key in dictionary.keys():
      dictkeys += key
  print("sum of keys: ",dictkeys)    
  for value in dictionary.values():
        dictvalues += value  
  print("sum of values: ",dictvalues) 
sum_dict(dictionary)
 