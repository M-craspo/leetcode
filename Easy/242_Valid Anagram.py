class Solution(object):
    def isAnagram(self, s, t):
       s,t = sorted(s),sorted(t)
       return s == t 
        