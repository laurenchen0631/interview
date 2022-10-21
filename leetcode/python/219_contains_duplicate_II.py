class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        bucket = set[int]()
        for i in range(min(k+1, len(nums))):
            if nums[i] in bucket:
                return True
            bucket.add(nums[i])
        
        for i in range(k+1, len(nums)):
            bucket.remove(nums[i-k-1])
            if nums[i] in bucket:
                return True
            bucket.add(nums[i])
        return False

s = Solution()
print(s.containsNearbyDuplicate([1,2,3,4,2], 3))
print(s.containsNearbyDuplicate([1,0,1,1], 1))


        