class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        l: int = 0
        res: int = 0
        prod: int = 1
        for i, n in enumerate(nums):
            prod *= n
            while l <= i and prod >= k:
                prod /= nums[l]
                l += 1
            res += i - l + 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.numSubarrayProductLessThanK([10,5,2,6], 100))
    print(s.numSubarrayProductLessThanK([1,2,3], 0))