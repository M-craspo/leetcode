class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter = set(nums1) & set(nums2)  # find common elements using set intersection
        return list(inter)  
s = Solution()
print(s.intersection([4,9,5], [9,4,9,8,4]))