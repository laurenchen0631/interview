import bisect


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        r = l = bisect.bisect_left(arr, x)
        for _ in range(k):
            if l > 0 and (r == len(arr) or x - arr[l - 1] <= arr[r] - x):
                l -= 1
            elif r < len(arr):
                r += 1
        return arr[l:r]
s = Solution()
print(s.findClosestElements([1,2,3,4,5], 4, 3))
print(s.findClosestElements([1,2,3,4,5], 2, 0))
print(s.findClosestElements([1,2,3,4,5], 1, 6))
print(s.findClosestElements([1,2,3,4,5], 0, 6))
        