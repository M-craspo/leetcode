class Solution(object):
    def myAtoi(self, s):
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1
        num = []
        if not s:
            return 0
        s = s.strip()
        

        sign = 1
        if s and s[0] in ["-", "+"]:
            if s[0] == "-":
                sign = -1
            s = s[1:]  
        

        if not s or not s[0].isdigit():
            return 0
        

        for i in s:
            if i.isdigit():
                num.append(i)
            else:
                break
        

        try:
            num = int("".join(num)) * sign
        except ValueError:
            return 0

        if num < MIN_INT:
            return MIN_INT
        elif num > MAX_INT:
            return MAX_INT
        else:
            return num

# Test cases
s = Solution()
print(s.myAtoi("-"))          # Expected output: 0
print(s.myAtoi("42"))         # Expected output: 42
print(s.myAtoi("   -42"))     # Expected output: -42
print(s.myAtoi("4193 with words"))  # Expected output: 4193
print(s.myAtoi("words and 987"))    # Expected output: 0
print(s.myAtoi("-91283472332"))     # Expected output: -2147483648 (clamped)
