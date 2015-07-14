"""
Permutations with Duplicates

write a method to compute all permutations of a string whose characters are not necessarily unique.
 the list of permutations should not have duplicates
"""

# 1 notice details
"""repeated characters"""
# 2 example
"""
1, 1, 1, 2, 2, 2, 3
"""
# 3 brute force



# 4 optimize
"""
1. go through list, put items into dictionary, use this dictionary to create permutations of unique characters
2. pick first character, then solve subproblem of permutations of remaining characters
"""
# 5 walk through
# 6 implement
def printPerms(s):
	result = []
	map = buildFreqTable(s)
	printPermsWork(map, [], len(s), result)
	return result

def buildFreqTable(s):
	map = {}
	for c in s:
		if c not in map:
			map[c] = 1
		else:
			map[c] += 1
	return map

def printPermsWork(map, prefix, remaining, result):
	if remaining == 0:
		result.append(prefix)
		return;

	for c in map:
		count = map[c]
		if count > 0:
			map[c] = count - 1
			unique_prefix = list(prefix)
			unique_prefix.append(c)
			printPermsWork(map, unique_prefix, remaining - 1, result)
			map[c] = count


# 7 test
s = [1, 2, 2]
print printPerms(s)