class Solution:
    def climbStairs(self, n):
        if n <= 2 :
            return n
              
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        
        return b
# Example usage
solution = Solution()
#print(solution.climbStairs(2))  # Output: 2
#print(solution.climbStairs(3))  # Output: 3
print(solution.climbStairs(10))  # Output: 5
