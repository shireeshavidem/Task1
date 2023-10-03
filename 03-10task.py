# 1.Write a Python program to unpack a tuple into several variables.
#create a tuple
tuple_1 = 4, 8, 3 
print(tuple_1)
n1, n2, n3 = tuple_1
#unpack a tuple in variables
print(n1 + n2 + n3) 
print(n1)

# 2.Write a Python program to add an item to a tuple.
#create a tuple
t = (10,40,50,70,90) 
print(t)
t = t + (20,)
print(t)
#converting the tuple to list
l = list(t) 
#use different ways to add items in list
l.append(30)
t = tuple(l)
print(t)

# 3.Write a Python program to convert a tuple to a string.
#  Ex:tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
print(type(tup))
def convertTuple(tup):
    str = ''.join(tup)
    return str
str = convertTuple(tup)
print(str,type(str))    

# 4.Write a Python program to get the specified element from the last element of a tuple.
tuple_2 = ('p','y','t','h','o','n',1,2,3)
t = tuple_2[3]
print(t)

# 5.Write a Python program to add member(s) to a set.
colors = {"red"}
#addding single element
colors.add("blue")
print(colors)
#adding multiple elements
colors.update(["green","yellow","black"])
print(colors)

# 6.Write a Python program to create an intersection of sets.
#Intersection prints only commom elements
set1 = {10,20,30,40}
set2 = {20,80,70,100}
set1set2Intersection = set1&set2
print(set1set2Intersection)

#7.Write a Python program to create a union of sets.
#union prints without common elements
set1set2Union = set1|set2
print(set1set2Union)

#8.Write a Python program to create set difference.
#Difference prints removes common element from both sets and returns set1
set1set2Difference = set1-set2
print(set1set2Difference)

#9.Write a Python program to create a symmetric difference.
#symmetric difference removes common elements and returns both sets
set1set2SymmetricDiff = set1^set2
print(set1set2SymmetricDiff)

#10.Write a Python program to find the maximum and minimum values in a set.
set = {1,2,3,4,5,6,7,8,9}
print(min(set))
print(max(set))