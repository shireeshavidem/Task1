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
    sum = sum + list[i]
print(sum)

#using while loop
lst = [11,5,17,18,23]
i = sum = 0
while(i < len(lst)):
    sum = sum + lst[i]
    i += 1
print(sum)    