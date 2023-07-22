class Solution:
    def isGood(self, nums: list[int]) -> bool:
        n = len(nums) - 1
        checked = [0] * (n + 1)
        for num in nums:
            if num > n:
                return False
            
            checked[num] += 1
            if num == n:
                if checked[num] > 2:
                    return False
            elif checked[num] > 1:
                return False
        return True
        
        
s = Solution()
print(s.isGood([1,3,3,2]))