"""
Permutations without Dups

write a method to compute all permutations of a string of unique characters
"""

# 1 notice the unique details
# 2 work on an example
# 3 brute force solution
"""
linear go through list, select first char, second char etc.
"""
def Recursive_Permutation(chars):
	all_permutations = []
	if len(chars) == 0: 
		all_permutations.append([])
		return all_permutations

	first_char = chars[0]
	remaining_chars = [c for c in chars if c != first_char]

	other_permutations = Recursive_Permutation(remaining_chars)
	for p in other_permutations:
		for i in xrange(len(p)+1):
			unique_p = list(p)
			unique_p.insert(i, first_char)
			all_permutations.append(unique_p)
			# print permutation
	return all_permutations

"""SOLUTION 2"""
def Other_Recursive_Permutation(chars):
	all_permutations = []
	if len(chars) == 0:
		all_permutations.append([])
		return all_permutations

	for i in xrange(len(chars)):
		remaining_chars = [c for c in chars if c != chars[i]]
		other_permutations = Other_Recursive_Permutation(remaining_chars)
		for p in other_permutations:
			unique_p = list(p)
			unique_p.insert(0, chars[i])
			all_permutations.append(unique_p)

	return all_permutations

"""SOLUTION 3"""
def Third_Recursive_Permutation(chars):
	result = []
	Third_Recursive_Permutation_Work([], chars, result)
	return result

def Third_Recursive_Permutation_Work(prefix_chars, remainder_chars, result):
	if len(remainder_chars) == 0:
		result.append(prefix_chars)

	for i in xrange(len(remainder_chars)):
		less_chars = [c for c in remainder_chars if c != remainder_chars[i]]
		new_prefix_chars = list(prefix_chars)
		new_prefix_chars.append(remainder_chars[i])
		Third_Recursive_Permutation_Work(new_prefix_chars, less_chars, result)

# 4 optimize
# 5 walk through optimized algorithm
# 6 implement
# 7 test
chars = [1, 2, 3]
print Recursive_Permutation(chars)
print Other_Recursive_Permutation(chars)
print Third_Recursive_Permutation(chars)