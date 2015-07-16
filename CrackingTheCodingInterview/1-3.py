"""
Urlify

replace spaec in string with %20
given the true length of the string
"""

# 1 notice details
"""
Given the true length of the string
"""
# 2 work on example
# 3 1st solution
"""
0. find first non space char
1. start moving and subtracting 1 from the true length of the string
2. if a space
	if just_replaced = true, take out space, bool just_replaced = true
	if just_replaced = false, replace with %20, bool just_replaced = true
3. if a char
	just_replaced = false
4. if at end of string
	if true length > 0, not possible, throw error
	return function
5. if true length == 0
	if next char is a non space character, not possible, throw error
	return function
"""
# 4 optimize with unused details
"""
walk through string backwards
"""
# 5 walk through optimization
# 6 implement optimization
def Replace_Spaces(sentence, length):
	space_count = 0
	for i in xrange(length):
		if sentence[i] == ' ':
			space_count += 1

	new_length = length + space_count * 2
	new_sentence = ['_'] * new_length
	for i in xrange(length - 1, -1, -1):
		if sentence[i] == ' ':
			new_sentence[new_length - 1] = '0'
			new_sentence[new_length - 2] = '2'
			new_sentence[new_length - 3] = '%'
			new_length -= 3
		else:
			new_sentence[new_length - 1] = sentence[i]
			new_length -= 1

	return new_sentence

# 7 test
sentence = list("Mr John Smith     ")
print ''.join(Replace_Spaces(sentence, 13))