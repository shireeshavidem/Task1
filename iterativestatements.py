#Iterative statements

# 1.program for While loop
x = 0
while (x < 5):
   print(x)
   x = x + 1


# 2.program for While loop with else 
x = 1
while (x < 5):
   print('inside while loop value of x is ',x)
   x = x + 1
else:
   print('inside else value of x is ', x) 

# 3.program for For loop   
for letter in"python":
 print("The current letter:", letter)

# 4.program for Nested loop
rows = 5
# outer loop
for i in range(1, rows + 1):
    # inner loop
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')

# 5.program for Nested for loop

for i in range(2, 4):

	# Printing inside the outer loop
	# Running inner loop from 1 to 10
	for j in range(1, 11):

		# Printing inside the inner loop
		print(i, "*", j, "=", i*j)
	# Printing inside the outer loop
	print()