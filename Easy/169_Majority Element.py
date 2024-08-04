from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        count = Counter(nums)
        return max(count.keys(), key=count.get)
        
        