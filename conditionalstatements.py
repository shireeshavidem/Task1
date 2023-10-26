# Conditional statements
# 1. program for if statement
a = 10  
b = 20  
if a<b:  
  print("a is less than b")

# 2.program for if else statement
letter = "A"

if letter == "B":
 print("letter is B")

else:
    if letter == "C":
        print("letter is C")
   
    else:
      if letter == "A":
	      print("letter is A")
      else:
         print("letter isn't A, B and C")
          

	
 

# 3.program for elif statement
num = 10
if (num == 0):
     print("Number is Zero")
 
elif (num > 5):
       print("Number is greater than 5")
 
else:
       print("Number is smaller than 5")
             

# 4.program for Nested if statement
num = 10

if num > 5:
 print("Bigger than 5")

if num <= 15:
 print("Between 5 and 15")

# 5.program for if elif statement

letter = "A"

if letter == "B":
	print("letter is B")

elif letter == "C":
	print("letter is C")

elif letter == "A":
	print("letter is A")

else:
	print("letter isn't A, B or C")