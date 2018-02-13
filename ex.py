def keep_ints(cond):
	def helper(n):
		k = 1
		while k <= n:
			if cond(k):
				print(k)
			k += 1
	return helper
	

def outer(n):
	def inner(m):
		return n - m
	return inner

def repeat(f, x):
	while f(x) != x:
		x = f(x)
	return x

def g(y):
	return (y + 5) // 3

