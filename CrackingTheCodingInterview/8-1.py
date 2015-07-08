"""
Triple Step:
n steps total
1 step, 2 steps and 3 steps at a time
how many ways
"""

# My solution
def Recur_Walk_Steps(kinds_of_steps, steps_to_go, known_ways):
	count = 0

	if steps_to_go == 0:
		return 1
	elif known_ways[steps_to_go] > 0:
		return known_ways[steps_to_go] 
	else:
		for s in [step for step in kinds_of_steps if step <= steps_to_go]:
			count += Recur_Walk_Steps(kinds_of_steps, steps_to_go - s, known_ways)

	known_ways[steps_to_go] = count
	return count

# SOLUTION:
def countWays(n):
	memo = [-1] * (n + 1)
	return countWaysWork(n, memo)

def countWaysWork(n, memo):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	elif memo[n] > -1:
		return memo[n]
	else:
		memo[n] = countWaysWork(n-1, memo) + countWaysWork(n-2, memo) + countWaysWork(n-3, memo)
		return memo[n]

steps_to_go = 37
known_ways = [0] * (steps_to_go + 1)
print Recur_Walk_Steps([1, 2, 3], steps_to_go, known_ways)
print countWays(steps_to_go)