"""
Parens

implement an algorithm to print all valid combinations of n pairs of parentheses
((())), (()()), (())(), ()(()), ()()()
"""
# 1 notice detials
"""
I know how to check for matching parentheses using a stack
"""
# 2 example
"""
n = 0
None

n = 1
()

n = 2
(()), ()()

n = 3
((())), (()()), (())(), ()(()), ()()()

How would I solve this by hand?
"""
# 3 brute force
"""
Try inserting () into different positions
Use a dictionary to keep track of repetitions
"""
def Parens_Combo(n):
	all_combo_set = set()

	if n == 0:
		all_combo_set.add("")
	else:
		prev_set = Parens_Combo(n-1)
		for s in prev_set:
			for i in xrange(len(s)):
				if s[i] == "(":
					new_s = s[:i+1] + "()" + s[i+1:]
					all_combo_set.add(new_s)
			all_combo_set.add("()" + s)

	return all_combo_set	


# 4 optimize
"""
We waste a lot of time making duplicates and insert the dups into result set
"""
# 5 walk through algorithm
# 6 implement
def addParen(combo_list, leftRem, rightRem, str, count):
	if leftRem < 0 or rightRem < leftRem:
		return

	if leftRem == 0 and rightRem == 0:
		s = str
		combo_list.append(s)
	else:
		if leftRem > 0:
			new_str = str[:count] + '(' + str[count+1:]
			addParen(combo_list, leftRem-1, rightRem, new_str, count+1)

		if rightRem > leftRem:
			new_str = str[:count] + ')' + str[count+1:]
			addParen(combo_list, leftRem, rightRem-1, new_str, count+1)

def generateParens(count):
	combo_list = []
	str = ""
	addParen(combo_list, count, count, str, 0)
	return combo_list

# 7 test
n = 3
print Parens_Combo(n)
print generateParens(n)