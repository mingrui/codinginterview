"""
Recursive multiply:
write a recursive function to multiply two numbers without * and /
can use addition, substraction and bit shifting, minimize the number of these operations
"""

# 1 details: minimize the number of operations
# 2 example: 8 * 7
# 3 brute force: 8 + 8 + ... + 8, time: O(n), space: O(n) on the stack
def Brute_Multiply(first_num, second_num):
	answer_sign = 1

	if first_num == 0 or second_num == 0:
		return 0
	
	if (first_num < 0 and second_num > 0) or (first_num > 0 and second_num < 0):
		answer_sign = -1

	if first_num < 0:
		first_num = -first_num
	if second_num < 0:
		second_num = -second_num

	answer = Brute_Multiply_Work(first_num, second_num)

	if answer_sign == -1:
		answer = -answer

	return answer


def Brute_Multiply_Work(first_num, second_num):
	if second_num <= 1:
		return first_num
	else:
		return first_num + Brute_Multiply_Work(first_num, second_num - 1)

# 4 optimize:
"""
A)
1. compute half, then other half
2. memoize stepping stone results to the final answer

B)
1. 8 + 16 + 32 etc... the smaller number always devide by 2, recursively will be 2^n
   we can achieve this with bit shifting
"""

# 5 walk through:

# 6 implement:
def Better_Multiply(first_num, second_num):
	bigger = first_num if first_num > second_num else second_num
	smaller = first_num if first_num < second_num else second_num
	return Better_Multiply_Work(bigger, smaller)

def Better_Multiply_Work(bigger, smaller):
	if smaller == 0:
		return 0
	elif smaller == 1:
		return bigger

	s = smaller >> 1 # divide by 2
	halfProduct = Better_Multiply_Work(bigger, s)

	if smaller % 2 == 0:
		return halfProduct + halfProduct
	else:
		return halfProduct + halfProduct + bigger

# 7 test:

print Brute_Multiply(8, 7)
print Better_Multiply(8, 7)