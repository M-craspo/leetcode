class Solution(object):
    def isPalindrome(self, s):
        x = ''.join(char for char in s if char.isalnum()).lower()
        return x == x[::-1]

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))