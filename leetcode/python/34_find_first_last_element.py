class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        leftmost = rightmost = -1
        ll = rl = 0
        lr = rr = len(nums) - 1

        while ll <= lr:
            m = (ll + lr) // 2
            if nums[m] < target:
                ll = m + 1
            elif nums[m] > target:
                lr = m - 1
            else:
                leftmost = m
                lr = m - 1

        while rl <= rr:
            m = (rl + rr) // 2
            if nums[m] < target:
                rl = m + 1
            elif nums[m] > target:
                rr = m - 1
            else:
                rightmost = m
                rl = m + 1
        
        return [leftmost, rightmost]

if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10], 8))
    print(s.searchRange([5,7,7,8,8,10], 6))
    print(s.searchRange([], 0))
    print(s.searchRange([1,1,1,1,1], 1))
        