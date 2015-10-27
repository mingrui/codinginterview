class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        ans = 0
        for e in s:
            ans = ans * 26 + ord(e) - ord('A') + 1
        return ans