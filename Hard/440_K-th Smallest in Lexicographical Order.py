class Solution(object):
    #At the root is 1, and its children are 10, 11, 12, ..., 19.
    #The node 2 has children 20, 21, ..., 29, and so on.
    
    def count_numbers(self, a, b, n):
        """ 1- This function counts how many numbers lie between a and b in the lexicographical tree, 
            considering numbers up to n. 
            2- It multiplies a and b by 10 at each step to explore the next level of the tree."""
        count = 0
        
        while a <= n:
            count += min(n + 1, b) - a
            a *= 10
            b *= 10
        return count
    def findKthNumber(self, n, k):
        num = 1
        i = 1
        while i < k:
            count = self.count_numbers(num, num + 1, n)
            if i + count <= k:
                i += count
                num += 1
            else:
                i += 1
                num *= 10
        return num

s = Solution()
print(s.findKthNumber(13, 2))