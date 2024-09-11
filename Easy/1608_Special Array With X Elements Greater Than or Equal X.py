class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)   
        n = len(nums)
        
        for x in range(n + 1):
            if x == 0 and nums[-1] >= x:
                return 0
            elif x == n or nums[x-1] >= x > nums[x]:
                return x
        
        return -1

s = Solution()
print(s.specialArray([0,4,3,0,4]))