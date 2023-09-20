#Unconditional loops
# Break statement
for letter in"python":
     if letter=='h':
          
           break
     print(letter)
print("bye")

# Continue statement
for var in "shireesha":
	if var == "e":
		continue
	print(var)
     
# pass statement

s = "shireesha"

# Empty loop
for i in s:
	# No error will be raised
	pass

# Empty function
def fun():
	pass

# No error will be raised
fun()

# Pass statement
for i in s:
	if i == 'h':
		print('Pass executed')
		pass
	print(i)