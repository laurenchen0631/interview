class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        nums = set[int]()
        for n in arr:
            if n * 2 in nums or n / 2 in nums:
                return True
            nums.add(n)
        return False

s = Solution()
print(s.checkIfExist([10,2,5,3]))
print(s.checkIfExist([7,1,14,11]))
print(s.checkIfExist([3,1,7,11]))