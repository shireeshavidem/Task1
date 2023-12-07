#1.write a python program to merge two lists.
list1 = ["mango","banana","apple","orange","guava"]
list2 = [120,60,100,40,50]

#using extend
list1.extend(list2)
print(list1)
#using concatenation
print(list1+list2)

#2.write a python program to find the sum of list elements.
list = [1,2,34,5]
sum = 0
for i in range(len(list)):
    sum = sum+list[i]
print(sum)

#using while loop
lst = [11,5,17,18,23]
i = sum = 0
while(i < len(lst)):
    sum = sum + lst[i]
    i += 1
print(sum)   

#3.write a python program to print even and odd numbers seperatly in list.
lst = [1,2,3,4,5,6,7,8,9]
even = []
odd = [] 
for i in lst:
 if(i%2 == 0):
    even.append(i)
 else:
    odd.append(i)
print(even)
print(odd)

#using list comprehension 
lst1 = [1,2,3,4,5,6,7,8,9,0]
def split(lst1):
   ev_lst = [ i for i in lst1 if i%2 == 0]
   odd_lst = [i for i in lst1 if i%2 != 0]
   print(ev_lst)
   print(odd_lst)
split(lst1)  

#4.write a python program to delete element of given index in list.
#using del list[index]
lst_1 = ["red","yellow","blue","green","white",1,2,3,4,5]
del lst_1[1:2]
print(lst_1)

#using pop(index)
lst_1.pop(6)
print(lst_1)

#5.write a python program to delete given elemet from the list 
#remove()
lst_1.remove("blue")
print(lst_1)

#del()
# lst_1.clear()
# print(lst_1)

#6.write a python program to insert an element at given index location.
lst_1[1] = "black"
print(lst_1)

#using insert()
lst_1.insert(3,45)
print(lst_1)

#7.write a python program to check the sizes of given two lists are same.
#using sort() funtion
list1 = ["mango","banana","apple","orange","guava"]
list2 = ["red","yellow","blue","green","white"]
# list1.sort()
# list2.sort()
# if list1 == list2:
#    print("Sizes of the lists are same")
# else:
#    print("Sizes of the lists are not same")

#using for loop
# for i in range(len(list1)):
#    if list1[i] != list2[i]:
#       print("False")
#       break
# else:
#    print("True")   

#8.Write a Python function that takes two lists and returns True if they have at least one common member.
lst1 = [1,3,4,6]
lst2 = [2,5,7,8,3]
def common_mem(lst1,lst2):
  result = False
  for i in lst1:
    for j in lst2:
      if i == j:
        result = True 
        return result
print(common_mem(lst1,lst2))

#Write a Python program to remove a specified column from a given nested list.
# Original Nested list:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# After removing 1st column:
# [[2, 3], [4, 5], [1, 1]]
#using pop()
listA = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# [i.pop(0) for i in listA]
# print(listA)

#using del
for i in listA:
 del i[0]
print(listA)


# 9. Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350
lstA = [123,345,678]
# for i in lstA:
#   print(i, end="")
  

#using join()
def convert(lstA):
 s = [str(i) for i in lstA]
 res = int("".join(s))
 return res
print(convert(lstA))

#10.Write a Python program to remove duplicates from a list.
lsta = [7,1,2,5,7,7,8,3,6,4]
lstb = []
for i in lsta:
  if i not in lstb:
   lstb.append(i)
print(lstb)  