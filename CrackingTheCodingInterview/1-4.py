"""
Palindrome Permutation

given a string, write a function to check if it is a permutation of a Palindrome
the palindrome does not need to be limited to just dictionary words
ingnore white spaces
"""

# 1 details
# 2 example
# 3 1st solution
"""
0. use hash table to track characters
1. see character, update hash table
	if hash table value is 0, add 1
	if hash table value is 1, subtract 1
2. in the end, hash table should only contain 1 char with count 1
"""
# 4 optimize
"""
A. as we go through the list and update the hash table, we can also keep track the number of odd counts
	if the odd counts are more than 1, then we know sentence is not Palindrome

B. use a bit vector to keep track, than check the result bit vector if it has more than one "1" bit
"""
# 5 walk through optimization
# 6 implement
def Check_Palindrome_Permutation(sentence):
	bit_vector = 0
	for c in sentence:
		char_num = ord(c) - ord('a')
		bit_vector = Toggle_Bit(bit_vector, char_num)

	return bit_vector == 0 or Exactly_One_Bit(bit_vector)

def Toggle_Bit(bit_vector, index):
	if index < 0 :
		return bit_vector

	mask = 1 << index
	if bit_vector & mask == 0 :
		# bit_vector and mask does not have 1 in the same place, record that 1 in bit_vector
		bit_vector |= mask
	else:
		# bit_vector and mask have 1 in the same place, make that one into a zero
		bit_vector &= ~mask
	
	return bit_vector

def Exactly_One_Bit(bit_vector):
	return bit_vector & (bit_vector - 1) == 0

# 7 test
print Check_Palindrome_Permutation("tta")