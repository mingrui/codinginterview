"""
Towers of Hanoi
"""

# 1 notice the details
# 2 work on one example
# 3 brute force solution
# 4 optimize
# 5 walk through algorithm
# 6 implement
def Solve_Hanoi(height, from_pole, to_pole, mid_pole):
	if height > 0:
		Solve_Hanoi(height - 1, from_pole, mid_pole, to_pole)
		Move(from_pole, to_pole)
		Solve_Hanoi(height - 1, mid_pole, to_pole, from_pole)

def Move(from_pole, to_pole):
	print("move disk from", from_pole, "to", to_pole)

# 7 test
Solve_Hanoi(3, "A", "B", "C")