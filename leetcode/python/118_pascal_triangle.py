class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal: list[list[int]] = [[1]]
        for i in range(1, numRows):
            pascal.append([1])
            for j in range(1, i):
                pascal[-1].append(pascal[i-1][j-1]+pascal[i-1][j])
            pascal[-1].append(1)

        return pascal

s = Solution()
print(s.generate(5))
