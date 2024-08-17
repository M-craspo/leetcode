from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = Counter(s)
        for i, char in enumerate(s):
            if x[char] == 1:
                return i
        return -1
s = Solution()
print(s.firstUniqChar("loveleetcode"))