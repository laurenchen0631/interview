class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        i = j = 0
        res: list[list[int]] = []
        while i < len(firstList) and j < len(secondList):
            if firstList[i][1] < secondList[j][0]:
                i += 1
            elif secondList[j][1] < firstList[i][0]:
                j += 1
            else:
                res.append([
                    max(firstList[i][0], secondList[j][0]),
                    min(firstList[i][1], secondList[j][1]),
                ])
                if res[-1][1] == firstList[i][1]:
                    i += 1
                else:
                    j += 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
    print(s.intervalIntersection([[1,3],[5,9]], []))