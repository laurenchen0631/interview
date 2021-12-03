class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: list[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

if __name__ == '__main__':
    s = Solution()
    a = [1,2,3,4,5,6,7]
    s.rotate(a, 3)
    print(a)

    b = [-1,-100,3,99]
    s.rotate(b, 2)
    print(b)