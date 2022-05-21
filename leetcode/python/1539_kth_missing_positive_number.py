class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (l+r) // 2
            missing = arr[m] - (m+1)
            if missing < k:
                l = m+1
            else:
                r = m-1
        return l + k

s = Solution()
print(s.findKthPositive(arr = [2,3,4,7,11], k = 5))
print(s.findKthPositive(arr = [1,2,3], k = 5))
        