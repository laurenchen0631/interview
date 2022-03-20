from tkinter import E


class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        c1 = self.helper(tops, bottoms, tops[0])
        c2 = self.helper(tops, bottoms, bottoms[0])

        return min(c1, c2) if min(c1, c2) != len(tops) + 1 else -1

    def helper(self, tops: list[int], bottoms: list[int], target: int) -> int:
        count = [0, 0]
        for i in range(len(tops)):
            if target != tops[i] and target != bottoms[i]:
                return len(tops) + 1
            if target != tops[i]:
                count[0] += 1
            if target != bottoms[i]:
                count[1] += 1
        return min(count)

s = Solution()
print(s.minDominoRotations(tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]))
print(s.minDominoRotations(tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]))
print(s.minDominoRotations([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2]))