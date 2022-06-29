class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda p: (-p[0], p[1]))
        q: list[list[int]] = []
        for p in people:
            q.insert(p[1], p)
        return q

s = Solution()
print(s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
        