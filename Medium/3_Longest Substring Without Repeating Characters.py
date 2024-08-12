class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s :
            return 0
        char_index = {}
        start = 0
        max_len = 0
        for end, char in enumerate(s):
            if char in char_index and char_index[char] >=start :
                start = char_index[char] +1
            else:
                max_len = max(max_len, end - start + 1)
            char_index[char] = end
        return max_len
        
s = Solution()
print(s.lengthOfLongestSubstring('pwwkew'))