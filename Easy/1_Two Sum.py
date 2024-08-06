class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums and nums.index(complement) != i:   
                return i,nums.index(complement)
            
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))