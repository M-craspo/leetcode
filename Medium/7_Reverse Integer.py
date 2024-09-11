class Solution(object):
    def reverse(self, x):
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1

        if x == 0:
            return 0
        
        sign = 1 if x > 0 else -1

        x = abs(x)
        reversed_x = int(str(x)[::-1])
        result = sign * reversed_x
        if result > MAX_INT or result < MIN_INT:
            return 0
        
        return result