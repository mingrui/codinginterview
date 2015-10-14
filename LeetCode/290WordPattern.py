# build a "a" to "dog" dictionary and a "dog" to "a" dictionary
# use these 2 dictionaries to check for pattern

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern_list = list(pattern)
        word_list = str.split(" ")
        if len(word_list) != len(pattern_list):
        	return False
        length = len(pattern_list)
        comp_dict = {}
        for i in xrange(length):
        	if pattern_list[i] in comp_dict:
        		if comp_dict[pattern_list[i]] != word_list[i]:
        			return False
        	else:
        		comp_dict[pattern_list[i]] = word_list[i]

        reverse_comp_dict = {}
        for i in xrange(length):
        	if word_list[i] in reverse_comp_dict:
        		if reverse_comp_dict[word_list[i]] != pattern_list[i]:
        			return False
        	else:
        		reverse_comp_dict[word_list[i]] = pattern_list[i]
        return True


test_str = "dog dog cat cat"
sol = Solution()
print sol.wordPattern("aabb", test_str)