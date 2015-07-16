"""
One Away

there are three types of edits that can be performed on strings:
1. insert a char
2. remove a char
3. replace a char
given two strings, check if they are one edit(or zero edits) away
"""

# 1 mark details
# 2 example
# 3 1st solution
"""
False if there is more than 1 char difference
1. start from both left and right, start from left first
2. go until first difference, then start from right
3. go until first difference, stop
4. check if the difference is in the same place
"""
# 4 optimize
# 5 walkthrough
# 6 implement
def One_Away(sOne, sTwo):
	if abs(len(sOne) - len(sTwo)) > 1:
		return False

	smallerS = sOne
	biggerS = sTwo
	if len(sOne) > len(sTwo):
		smallerS = sTwo
		biggerS = sOne

	# start check from left
	left_diff_index = -1
	for i in xrange(len(smallerS)):
		if smallerS[i] != biggerS[i] :
			left_diff_index = i
			break

	# check all smallerS, all match and string len difference is <= 1
	# must be true
	if left_diff_index == -1:
		return True

	right_diff_index = -1
	si = len(smallerS) - 1
	bi = len(biggerS) - 1
	while si >= 0 and bi >= 0 :
		if smallerS[si] != biggerS[bi] :
			right_diff_index = bi
			break
		si -= 1
		bi -= 1

	print left_diff_index
	print right_diff_index

	return left_diff_index == right_diff_index

# 7 test

print One_Away("pall", "pael")