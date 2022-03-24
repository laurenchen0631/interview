class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        l: int = 0
        r:int = len(people) - 1
        count: int = 0
        while l <= r:
            if l < r and people[r] + people[l] <= limit:
                l += 1
            r -= 1
            count += 1
        return count

s = Solution()
print(s.numRescueBoats(people = [1,2], limit = 3))
print(s.numRescueBoats(people = [3,2,2,1], limit = 3))
print(s.numRescueBoats(people = [3,5,3,4], limit = 5))
print(s.numRescueBoats(people = [1,2,4,5], limit = 6))
print(s.numRescueBoats([2,49,10,7,11,41,47,2,22,6,13,12,33,18,10,26,2,6,50,10], 50))