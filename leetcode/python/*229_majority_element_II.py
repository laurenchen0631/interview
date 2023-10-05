class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        
        count1 = count2 = 0
        candidate1 = candidate2 = None
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        res = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums) // 3:
                res.append(c)
        return res