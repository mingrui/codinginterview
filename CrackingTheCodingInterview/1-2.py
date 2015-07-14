"""
Check Permutation

Given two strings, write a method to decide if one is a permutation of the other
"""

# 1 details
"""
permutation is the same characters arranged differently
"""
# 2 work on example
# 3 first "kinda good" solution that comes to mind
"""
use a hash map, go through first string, hash map for character + 1
go through second string, hash map character - 1
check if hash map items all equal to 0
O(2*n)
"""
# 4 optimize using overlooked details
# 5 walk through optimized algorithm
# 6 implement

def Check_Permutation(str_one, str_two):
	if len(str_one) != len(str_two):
		return False

	letter_appearance = {}
	for c in str_one:
		if c in letter_appearance:
			letter_appearance[c] += 1
		else:
			letter_appearance[c] = 1

	for c in str_two:
		if c in letter_appearance:
			letter_appearance[c] -= 1
			if letter_appearance[c] < 0:
				return False
		else:
			return False

	return True

# 7 test

print Check_Permutation("abc", "cba")
