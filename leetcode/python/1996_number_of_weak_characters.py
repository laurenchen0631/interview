class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        maxDefense: int = 0
        res: int = 0
        for _, defense in properties[::-1]:
            if defense < maxDefense:
                res += 1
            else:
                maxDefense = defense
        return res

s = Solution()
print(s.numberOfWeakCharacters([[5,5],[6,3],[3,6]]))
print(s.numberOfWeakCharacters([[2,2], [3,3]]))