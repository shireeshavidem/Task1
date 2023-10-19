def f1(): 
	s = 'Me too'
	def f2():
		s = 'I love python'
		print(s) 
	f2()
	print(s)


def Recur_facto(x):
    if (x == 0):
        return 1
    return x * Recur_facto(x-1)
print(Recur_facto(x=4))
