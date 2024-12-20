class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, len(s) - 1
        
        while left < right and s[left] == s[right]:
            char = s[left]
            while left <= right and s[left] == char:
                left += 1
            while left <= right and s[right] == char:
                right -= 1
                
        return right - left + 1
sol = Solution()
print(sol.minimumLength("aabccabba"))


