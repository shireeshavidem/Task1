#1.Write a python program to remove a given  character from string.
#using replace() 
string = input("Enter your string: ")
char = input("Enter the character you want remove from string: ")
print(string.replace(char,""))

#using translate()
string_1 = input("Enter your string: ")
character = input("Enter the character you want remove from string: ")
print(string_1.translate({ord(character): None}))

#2.Write a program to check String is Palindrome or not.
string_2 = input("Enter your string: ")
def ispalindrome(string_2):
    return string_2 == string_2[::-1]
if ispalindrome(string_2):
    print("yes")
else :
    print("no")

#3.Write a python program to check given character is vowel or consonant.
char = input("Enter a character : ") 
vowels = ["a","e","i","o","u","A","E","I","O","U"]
if char in vowels:
    print(f"'{char}' is a vowel")
else:
    print(f"'{char}' is a consonant")

#4.Write a python program to replace string space with given character in Python.
string_3 = input("Enter your string: ")
character = input("Enter a character: ")
print(string_3.replace(" ",character))

#5.Write a python program to count alphabets, digits, and special characters in the string.
string_4 = input("Enter your string: ")
alphabets=digits=special=0
for i in range(len(string_4)):
     if (string_4[i].isalpha()):
         alphabets = alphabets + 1
     elif (string_4[i].isdigit()):
         digits = digits + 1
     else:
         special = special + 1
print(alphabets)
print(digits)
print(special)

#6.Write a python program to remove all the blank spaces in a given string.
string_5 = input("Enter your string: ")
print(string_5.translate({ord(" "): None}))

#7.Write a python program to find sum of integers in the string.
str1 = input("Enter your string: ")
def sum_digits_string(str1):
    sum_digit = 0
    for i in str1:
        if i.isdigit():
            x = int(i)
            sum_digit = sum_digit + x
    return sum_digit
print(sum_digits_string(str1))

#8.Write a python program to Remove Repeated Character from String.
str2 = input("Enter your string: ")
new_str = ""
for i in str2:
    if i not in new_str:
        new_str = new_str + i
print(new_str)        

#9.Write a python program to count occurrence of given character in string. 
str3 = input("enter your string: ")
char = input("Enter a character: ")
print(str3.count(char))

#10.Write a python program to check string is anagrams or not in Python.
s3 = input("enter your string: ")
s4 = input("enter your string: ")
a = sorted(s3.lower())
b = sorted(s4.lower())
def isanagram():
    if a == b:
        print("Given strings are anagrams")
    else:
        print("Given strings are not anagrams")
print(isanagram())