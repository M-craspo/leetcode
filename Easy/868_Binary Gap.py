class Solution(object):
    def binaryGap(self, n):
        binary = bin(n)[2:] # Convert number to binary, removing the '0b' prefix
        x = binary.strip('0').split('1')
        return max(len(i) for i in x)
        
solution = Solution()
print(solution.binaryGap(22))    
print(solution.binaryGap(5))