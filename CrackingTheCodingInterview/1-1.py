"""
Is Unique

Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""
# 1 notice details
"""
can't use addiional data structures
"""
# 2 work out example
# 3 brute force solution
"""
check each character with the rest of the string, O(n^2)
"""
# 4 optimize using overlooked details
"""
1. Use a hash table
2. Use a bit vector instead of a hash table to save space
3. Sort the array first in O(n * log(n)) time
"""
# 5 walk through optimized algorithm
# 6 implement
"""
Bit vector solution
Assuming only using a to z lower case letters
"""
def Unique_Letters(sentence):
	checker = 0
	for c in sentence:
		val = ord(c) - ord('a')
		if checker & (1 << val) > 0 :
			return False
		checker |= (1 << val)
	return True
# 7 test

print Unique_Letters("abc")
print Unique_Letters("abcc")