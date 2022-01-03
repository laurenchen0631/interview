from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        nontrusters = set([i for i in range(1, n+1)])
        trustCount = defaultdict(int)
        for [truster, trustee] in trust:
            if truster in nontrusters:
                nontrusters.remove(truster)
            trustCount[trustee] += 1
        if len(nontrusters) == 1 and trustCount[(i := nontrusters.pop())] == n - 1:
            return i
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.findJudge(3, [[1,3],[2,3]]))
    print(s.findJudge(3, [[1,3],[2,3],[3,1]]))
    print(s.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))