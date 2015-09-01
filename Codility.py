def solution(a):
	"""

	"""
	y = len(a)/2
	while True:
		if check_balance(y, a):
			return y
		else:
			y = check_balance(y, a)
def check_balance(x, a):
	"""
	checks the balance at integer x
	"""
	if sum(a[:x]) == sum(a[:x]):
		return True
	elif sum(a[:x]) > sum(a[:x]):
		return x/2
	else:
		return x + (len(a)-x)/2


