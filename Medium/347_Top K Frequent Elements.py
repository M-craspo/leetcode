class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_dict = {} 
        for num in nums: 
            if num in freq_dict: 
                freq_dict[num] += 1 
            else: 
                freq_dict[num] = 1 
        sorted_elements = sorted(freq_dict, key=freq_dict.get, reverse=True) 
        return sorted_elements[:k]
            