x = 'this is a variable'

def f():
	global y
	y = 'this is a variable inside a function'
	print('f printing x:  '+x)

def g():
	print('g printing f(y): '+y)


f()
g()

print('printing y:   '+y)
