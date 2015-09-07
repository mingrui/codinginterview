"""
Group Anagrams

write a method to sort an array of strings so that all the anagrams are next to each
other
"""

# 1 notice details
"""
sub problem is comparing anagrams
only way to do so is sort the word alphabetically and then compare the string
"""
# 2 example
# 3 brute force
# 4 optimize
# 5 walkthrough algorithm
"""
use a dictionary to do bucket sort O(N * logN)
"""
# 6 implement
from collections import defaultdict

def GroupAnagrams(anagramList):
	sortDict = defaultdict(list)

	for anagram in anagramList :
		cList = [c for c in anagram]
		cList.sort()
		result = "".join(cList)
		sortDict[result].append(anagram)

	sortList = []
	for key, value in sortDict.iteritems():
		for anagram in value:
			sortList.append(anagram)

	return sortList



aList = ["are", "don", "nod", "ear", "era"]
print GroupAnagrams(aList)
