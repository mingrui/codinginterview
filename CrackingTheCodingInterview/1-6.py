"""
String Compression

Implement a method to perform basic string compression using the counts of repeated characters.
for example aabcccccaaa = a2b1c5a3.
If the compressed string would not become smaller than the original string, method returns the original string
Only use uppercase and lowercase (a - z)
"""

# 1 details
# 2 example
# 3 1st solution
"""
see char
	if char same as previous char, add to counter
	if char different as previous char, record previous char count, start new counter for this char
the result is put into a new string

use a list, then turn into a string
"""
# 4 optimize
# 5 verify
# 6 implement
def Compress(sentence):
	if len(sentence) <= 0:
		return

	result_list = []
	prev = sentence[0]
	count = 0
	for c in sentence:
		if c == prev:
			count += 1
		else:
			result_list.append(prev)
			result_list.append(str(count))
			prev = c
			count = 1
	result_list.append(prev)
	result_list.append(str(count))
	return result_list
# 7 test

print ''.join(Compress("aabcccccaaa"))