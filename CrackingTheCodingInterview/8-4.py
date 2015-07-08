"""
power set:
right a method to return all subsets of a set
"""

def Generate_All_Subset(master_set, index):
	subsets = []
	if len(master_set) == index:
		subsets.append([])
	else:
		subsets = Generate_All_Subset(master_set, index+1)
		item = master_set[index]
		more_subsets = []
		for s in subsets:
			new_subset = s + [item]
			more_subsets.append(new_subset)
		subsets.extend(more_subsets)

	return subsets

master_set = [1, 2, 3]

print Generate_All_Subset(master_set, 0)