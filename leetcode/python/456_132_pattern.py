class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False
        curMins = [nums[0]]
        for n in nums[1:]:
            curMins.append(min(curMins[-1], n))
        stack: list[int] = []
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == curMins[j]:
                continue
            while stack and stack[-1] <= curMins[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
        return False

s = Solution()
print(s.find132pattern([6,12,3,4,6,11,20]))