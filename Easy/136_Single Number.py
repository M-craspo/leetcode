class Solution(object):
    def singleNumber(self, nums):
        singlenum = []
        for num in nums:
            if num not in singlenum:
                singlenum.append(num)
            else:
                singlenum.remove(num)
        return singlenum[0]