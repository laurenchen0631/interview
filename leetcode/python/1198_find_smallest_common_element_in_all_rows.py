class Solution:
    def smallestCommonElement(self, mat: list[list[int]]) -> int:
        common = set(mat[0])
        for row in mat[1:]:
            common &= set(row)
            if not common:
                return -1
        return min(common)

s = Solution()
print(s.smallestCommonElement([[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]))
print(s.smallestCommonElement([[1,2,3],[2,3,4],[2,3,5]]))