class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        count = [0] * (n + 1)
        duplicate = missing = 0
        
        for num in nums:
            count[num] += 1
            if count[num] == 2:
                duplicate = num

        for i in range(1, n + 1):
            if count[i] == 0:
                missing = i
                break
                
        return [duplicate, missing]