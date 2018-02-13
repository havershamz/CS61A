#power function

def pow(x, n):
	product, k = 1, 0 
	while k < n:
		product, k = product * x, k+1
	return product

#root with newton update method

def find_zero(f, df):
	def near_zero(x):
		return approx_eq(f(x), 0)
	return improve(newton_update(f, df), near_zero)

def newton_update(f, df):
	def update(x):
		return x - f(x) / df(x)
	return update

def square_root_newton(a):
	def f(x):
		return x*x - a
	def df(x):
		return 2*x
	return find_zero(f, df)

def cube_root_newton(a):
	return find_zero(lambda x: x*x*x - a,
		lambda x: 3*x*x)

def root(a, n):
	def f(x):
		return pow(x, n) - a
	def df(x):
		return n * pow(x, n-1)
	return find_zero(f, df)


#root with fixed update method

def square_root_update(x, a):
	return (x + a/x) / 2

def cube_root_update(x, a):
	return(2 * x + a / (x * x)) / 3

def improve(update, close, guess = 1):
	while not close(guess):
		guess = update(guess) 
	return guess

def approx_eq(x, y, tolerance = 1e-15):
	return abs(x-y) < tolerance

def square_root(a):
	def update(x):
		return square_root_update(x, a)
	def close(x):
		return approx_eq(x*x, a)
	return improve(update, close) 

def cube_root(a):
	return improve(lambda x :cube_root_update(x, a),
		lambda x :approx_eq(x*x*x, a))

#function as return value

def summation(n, term):
	"""sum the first N terms of a sequence.

	>>> summation(5, cube)
	225
	"""
	total, k = 0, 1
	while k<=n:
		total, k = total + term(k), k+1
	return total

def make_adder(n):
	"""Returen a function that takes one argument 
	K and return K + N

	>>> add_three = make_adder(3)
	>>> add_three(4)
	7
	"""
	def adder(k):
		return k + n
	return adder	

#currying

def curry2(f):
	def g(x):
		def h(y):
			return f(x, y)
		return h
	return g 	

def uncurry2(g):
	def f(x,y):
		return g(x)(y)
	return f
 
def map_to_range(start, end, f):
 	while start < end:
 		print(f(start))
 		start = start + 1

#function decorators
def trace1(fn):
	def wrapped(x):
		print('->', fn, '(', x, ')')
		return fn(x)
	return wrapped

#rebindind to square = trace1(square) 
#trace1 takes in a fn as operand, which makes function
#"wrapped" can operate it. print sth. and return sth. like 
#fn(x)

@trace1
def square(x):
	return  x* x
@trace1
def sum_square_up_to(n):
	k, total = 1, 0
	while k<=n:
		total, k = total + square(k), k + 1
	return total 