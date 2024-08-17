from collections import Counter
class Solution(object):
    def isPossibleToSplit(self, nums):
        if len(nums)%2:
            return False
        x = Counter(nums)
        y = x.most_common(1)[0][1] #to take the value =2 only not (1,2)
        if y > 2:
            return False
        return True
s = Solution()
print(s.isPossibleToSplit([1,1,2,2,3,4]))