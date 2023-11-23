class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        res = []
        for i, j in zip(l, r):
            res.append(self.is_arithmetic(nums[i:j+1]))
        return res
    
    # 1, 2, 3, 4
    # 1, 3, 5, 9
    def is_arithmetic(self, nums: list[int]) -> bool:
        n = len(nums)
        counter = {}
        mini, maxi = nums[0], nums[0]
        for v in nums:
            counter[v] = counter.get(v, 0) + 1
            mini = min(mini, v)
            maxi = max(maxi, v)

        gap, rem = divmod(maxi - mini, n - 1)
        if rem != 0:
            return False

        prev = mini
        for i in range(1, n):
            next_value = prev + gap
            if next_value in counter and counter[next_value] > 0:
                counter[next_value] -= 1
                prev = next_value
            else:
                return False
                
        return True

