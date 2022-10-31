class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        outgoing = [set[int]() for _ in range(numCourses)]
        incoming = [0] * numCourses
        for i, j in prerequisites:
            outgoing[j].add(i)
            incoming[i] += 1
        q = [i for i in range(numCourses) if incoming[i] == 0]
        while q:
            i = q.pop()
            for j in outgoing[i]:
                incoming[j] -= 1
                if incoming[j] == 0:
                    q.append(j)
        return all(i == 0 for i in incoming)


s = Solution()
print(s.canFinish(numCourses = 2, prerequisites = [[1,0]]))