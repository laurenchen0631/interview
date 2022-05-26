# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        
        # check candidate is known by n-1 people
        for j in range(0, n):
            if candidate == j:
                continue
            if not knows(j, candidate) or knows(candidate, j):
                return -1
        return candidate