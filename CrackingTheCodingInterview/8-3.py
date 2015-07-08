"""
magic index
i in sorted distinct integers list A[0 ... n-1] such that A[i] = i
FOLLOW UP
what if values are not distinct
"""

# because list is shorted, use binary search
# figure out when to move left, when to move right

def Find_Magic_Index(magic_list, start_index, end_index):
	if start_index > end_index:
		return False

	search_index = start_index + (end_index - start_index) // 2

	if magic_list[search_index] > search_index:
		return Find_Magic_Index(magic_list, start_index, search_index-1)
	elif magic_list[search_index] == search_index:
		print search_index
		return True
	else:
		return Find_Magic_Index(magic_list, search_index+1, end_index)

def Find_Magic_Index_Indistinct(magic_list, start_index, end_index):
	if start_index > end_index:
		return False

	search_index = start_index + (end_index - start_index) // 2
	search_value = magic_list[search_index]
	if search_index == search_value:
		print search_index
		return True

	# search left
	leftIndex = min(search_index-1, search_value)
	leftFound = Find_Magic_Index_Indistinct(magic_list, start_index, leftIndex)
	# only return if true, because we need the right side to continue search
	if leftFound :
		return leftFound
	# search right
	rightIndex = max(search_index+1, search_value)
	right = Find_Magic_Index_Indistinct(magic_list, rightIndex, end_index)
	return right



magic_list = [-7, -6, -4, -3, -2, -1, 0, 3, 5, 7, 9, 10, 11, 13, 14]
indistinct_list = [-1, 2, 3, 4, 4, 4, 5, 5]
print Find_Magic_Index(magic_list, 0, len(magic_list)-1)
print Find_Magic_Index_Indistinct(indistinct_list, 0, len(indistinct_list)-1)