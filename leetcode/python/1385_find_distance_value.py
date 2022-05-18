class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        res = 0
        for n in arr1:
            i = self.findInsertIndex(arr2, n)
            leftWithinDistance = n - arr2[i-1] > d if i > 0 else True
            rightWithinDistance = arr2[i] - n > d if i < len(arr2) else True
            if leftWithinDistance and rightWithinDistance:
                print(n, arr2, i)
                res += 1
        return res

    def findInsertIndex(self, nums: list[int], n: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == n:
                return m
            elif nums[m] < n:
                l = m + 1
            else:
                r = m - 1
        return l

s = Solution()
print(s.findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2))
print(s.findTheDistanceValue(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3))
print(s.findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6))