from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        anagram_groups = defaultdict(list)
        
        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagram_groups[sorted_s].append(s)
        
        return list(anagram_groups.values())
s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))