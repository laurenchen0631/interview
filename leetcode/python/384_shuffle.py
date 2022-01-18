import random

class Solution:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.raw = nums.copy()

    def reset(self) -> list[int]:
        self.nums = self.raw.copy()
        return self.nums

    def shuffle(self) -> list[int]:
        for i in range(len(self.nums)):
            k = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[k] = self.nums[k], self.nums[i]
        return self.nums

s = Solution([1,2,3])
print(s.shuffle())
print(s.shuffle())
print(s.reset())
print(s.shuffle())
