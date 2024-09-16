class Solution(object):
    def findMinDifference(self, timePoints):
        minutes = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        
        # Check if there are duplicate times
        if len(minutes) != len(set(minutes)):
            return 0
        
        n = len(minutes)
        min_diff = float('inf')
        
        # Compare all adjacent pairs in a circular manner
        for i in range(n):
            diff = minutes[(i + 1) % n] - minutes[i]
            if diff <= 0:
                diff += 1440
            min_diff = min(min_diff, diff)
        
        return min_diff
s =Solution()
print(s.findMinDifference(["23:59","00:00"]))
print(s.findMinDifference(["00:00","23:59","00:00"]))
