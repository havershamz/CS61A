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

def left_binary_tree(tree):
	if type(tree) != list:
		return tree
	if len(tree) > 2:
		tree = [tree[:len(tree)-1], tree[len(tree)-1]]
	return [left_binary_tree(t) for t in tree]

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(list(set(nums)))
        return len(nums)

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if not prices or length == 1:
            return 0
        max_profit = 0
        temp_min = prices[0]
        j = 1
        while j < length:
            if prices[j] > temp_min:
                max_profit += prices[j] - temp_min
                temp_min = prices[j]
                j += 1
                continue
            if prices[j] <= temp_min:
                temp_min = prices[j]
                j += 1
        return max_profit

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if k >= length:
            k = length % k
        elif k != 0:
            position = length -k-1
            count = 0
            while count+1 < length:
                nums[0], nums[position] = nums[position], nums[0]
                position = (position + k) if ((position + k) < length) else (position + k - length)
                count += 1

a = Solution()
s = [1,2]
a.rotate(s, 2)
print(s)

"""a = [1 and 2,
2 and 1,
1 and 0,
0 and 1,
1 or 2,
2 or 1,
1 or 0,
0 or 1,
None or None]
print(a)"""