class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])

        res: list[list[int]] = []
        for l, r in intervals:
            if not res or res[-1][1] < l:
                res.append([l,r])
            else:
                res[-1][1] = max(r, res[-1][1])
        return res

if __name__ == '__main__':
    s = Solution()

    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(s.merge([[1,4],[4,5]]))
    print(s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))