from collections import deque

class Solution(object):
    def isValid(self, s):
        if len(s) == 1:
            return False
        stack = deque()
        mapping = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in mapping.values():  # Check if the char is an opening bracket
                stack.append(char)
            elif char in mapping:  # Check if the char is a closing bracket
                if not stack or mapping[char] != stack.pop():
                    return False
            else:
                return False  # Invalid character in the string
        return len(stack) == 0
solution = Solution()
print(solution.isValid("()"))  
       
    