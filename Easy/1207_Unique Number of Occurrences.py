from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        frq = Counter(arr)
        return len(set(frq.values())) == len(frq.values())
s = Solution()
print(s.uniqueOccurrences([1,2]))