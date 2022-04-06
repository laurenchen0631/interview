from typing import Counter


class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        ways: int = 0
        count = Counter(arr)
        nums = sorted(count)

        for i in range(len(nums)):
            t = target - nums[i]
            l = i
            r = len(nums) - 1
            while l <= r:
                if nums[l] + nums[r] < t:
                    l += 1
                    continue
                elif nums[l] + nums[r] > t:
                    r -= 1
                    continue
                elif i < l < r:
                    ways += count[nums[i]] * count[nums[l]] * count[nums[r]]
                elif i == l < r:
                    ways += count[nums[i]] * (count[nums[l]] - 1) // 2 * count[nums[r]]
                elif i < l == r:
                    ways += count[nums[i]] * count[nums[l]] * (count[nums[r]] - 1) // 2
                else:
                    ways += count[nums[i]] * (count[nums[l]] - 1) * (count[nums[r]] - 2) // 6
                l += 1
                r -= 1
        return ways % 1_000_000_007

s = Solution()
print(s.threeSumMulti(arr = [1,1,2,2,3,3,4,4,5,5], target = 8))
print(s.threeSumMulti(arr = [1,1,2,2,2,2], target = 5))

