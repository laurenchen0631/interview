class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (l+r) // 2
            if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
                return m
            elif arr[m-1] < arr[m] < arr[m+1]:
                l = m+1
            else:
                r = m
        return -1

s = Solution()
print(s.peakIndexInMountainArray(arr = [0,1,0]))
print(s.peakIndexInMountainArray(arr = [0,2,1,0]))
print(s.peakIndexInMountainArray(arr = [0,1,2,3,4,5,6,5]))
print(s.peakIndexInMountainArray([3,9,8,6,4]))