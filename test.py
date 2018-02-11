
def square_root_update(x, a):
	return (x + a/x) / 2

def cube_root_update(x, a):
	return(2* x + a / (x * x)) / 3

def improve(update, close, guess = 1):
	while not close(guess):
		guess = update(guess)
	return guess

def approx_eq(x, y, tolerance = 1e-14):
	return abs(x-y) < tolerance

def square_root(a):
	def update(x):
		return square_root_update(x, a)
	def close(x):
		return approx_eq(x *x, a)
	return improve(update, close) 

def cube_root(a):
	return improve(lambda x :cube_root_update(x, a),
		lambda x :approx_eq(x*x*x, a))
	