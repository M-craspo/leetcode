class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        nums = [1,2,3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        """
        def backtrack(start, end):
            # If we've reached the end of the array, add the current permutation
            if start == end:
                results.append(nums[:])  # Add a copy of nums to results
            for i in range(start, end):
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse with the next position in the array
                backtrack(start + 1, end)
                # Backtrack by swapping the elements back
                nums[start], nums[i] = nums[i], nums[start]

        results = []
        backtrack(0, len(nums))
        return results
solution = Solution()
print(solution.permute([1, 2, 3]))
