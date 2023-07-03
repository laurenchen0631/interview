from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal:
            return max(Counter(s).values()) >= 2
        
        diff = []
        for c1, c2 in zip(s, goal):
            if c1 != c2:
                diff.append((c1, c2))
        if len(diff) != 2:
            return False
        return diff[0] == diff[1][::-1]