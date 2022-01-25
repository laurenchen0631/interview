class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False
        startDownwards = False
        for i in range(1, len(arr)):
            delta = arr[i] - arr[i-1]
            if delta == 0:
                return False
            if not startDownwards and delta < 0:
                startDownwards = True
            elif startDownwards and delta > 0:
                return False
        return startDownwards and arr[1] - arr[0] > 0 # make sure at least one upward

s = Solution()
print(s.validMountainArray([0,3,2,1]))
print(s.validMountainArray([3,5,5]))
print(s.validMountainArray([3,2,1]))