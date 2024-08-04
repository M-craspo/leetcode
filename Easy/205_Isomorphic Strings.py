class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx)) # t.index(idx) find first index occurrence for char
        if map1 == map2:
            return True
        return False
solution = Solution()
print(solution.isIsomorphic('egg', 'add'))  # True