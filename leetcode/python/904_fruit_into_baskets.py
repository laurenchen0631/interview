class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        baskets = set[int]()
        res = l = last = 0
        for i, fruitType in enumerate(fruits):
            baskets.add(fruitType)
            if len(baskets) > 2:
                baskets = {fruits[last], fruitType}
                l = last
            res = max(res, i - l + 1)
            if fruitType != fruits[last]:
                last = i
        return res
    
s = Solution()
print(s.totalFruit([1,2,1]))
print(s.totalFruit([0,1,2,2]))
print(s.totalFruit([1,2,3,2,2]))
print(s.totalFruit([1,2,3,4,1,4,1]))
print(s.totalFruit([1,1,1,2,1,2,3,4,3,3,3,4,4,3]))
                
        