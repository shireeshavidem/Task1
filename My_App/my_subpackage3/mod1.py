
def func1(*args):
  for arg in args:
    print(arg)
	


def func2(**kwargs):
  for key, value in kwargs.items():
    print(key, value)


