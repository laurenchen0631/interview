class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        number = set[int]()
        for n in nums:
            if n in number:
                return True
            number.add(n)
        return False

s = Solution()
print(s.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))
print(s.containsDuplicate(nums = [1,2,3,4]))
        