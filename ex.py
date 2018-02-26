from ucb import trace
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

def fizz_buzz():
	i = 1
	while i <= 100:
		if not i % 3 or not i % 5:
			if not i % 15:
				print("fizz-buzz")
			elif not i % 3:
				print("fizz")
			else:
				print("buzz")
		else:
			print(i)
		i += 1

@trace
def gcd(m, n):
	"""return the greatest common devider
	>>> gcd(12, 8)
	4
	>>> gcd(16, 12)
	4
	>>> gcd(16, 8)
	8
	>>> gcd(2,16)
	2
	>>> gcd(5, 5)
	5
	"""
	if m % n == 0:
		return m
	elif m < n:
		return gcd(n, m)
	else:
		return gcd(m-n, n)


a = [1 and 2,
2 and 1,
1 and 0,
0 and 1,
1 or 2,
2 or 1,
1 or 0,
0 or 1,
None or None]
print(a)

