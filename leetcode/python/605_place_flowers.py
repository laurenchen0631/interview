class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        slots = [0] + flowerbed + [0]
        i: int = 1
        while n > 0 and i < len(slots) - 1:
            if slots[i] == 1:
                i += 2
            elif slots[i] == 0 and slots[i-1] == 0 and slots[i+1] == 0:
                n -= 1
                i += 2
            else:
                i += 1
        return n == 0

s = Solution()
print(s.canPlaceFlowers([1,0,0,0,1], n = 1))
print(s.canPlaceFlowers([1,0,0,0,1], n = 2))
print(s.canPlaceFlowers([0,1,0,0,0,0], n = 2))
print(s.canPlaceFlowers([1, 0], n = 1))
print(s.canPlaceFlowers([0,0,1,0,0], n = 1))
        