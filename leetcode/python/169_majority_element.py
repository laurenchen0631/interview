import random


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        while True:
            i = random.randrange(len(nums))
            k = nums[i]
            count: int = 0
            for e in nums:
                if e == k:
                    count += 1
            if count > len(nums) // 2:
                return k

    def boyerMoore(self, nums: list[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

s = Solution()
print(s.majorityElement([3,2,3]))
print(s.majorityElement([2,2,1,1,1,2,2]))