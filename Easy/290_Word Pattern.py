class Solution(object):
    def wordPattern(self, pattern, s):
        s1 = s.split(' ')
        if len(s1) != len(pattern):
            return False
        dict1 = {}
        dict2 = {}
        for i in range(len(pattern)):
            if pattern[i] not in dict1:
                dict1[pattern[i]] = s1[i]
            else:
                if dict1[pattern[i]] != s1[i]:
                    return False
            if s1[i] not in dict2:
                dict2[s1[i]] = pattern[i]
            else:
                if dict2[s1[i]] != pattern[i]:
                    return False