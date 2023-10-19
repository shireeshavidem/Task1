def f1(): 
	f1.s = 'I love python'
	def f2(): 
		f1.s = 'Me too'
		print(f1.s)


def recursive_factorial(n):
  if n == 1:
	  return n
  else:
	  return n * recursive_factorial(n-1)