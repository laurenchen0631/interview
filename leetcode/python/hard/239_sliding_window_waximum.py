from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if not nums or not k:
            return []
        if k == 1:
            return nums

        n = len(nums)
        q = deque()
        def cleanFor(i: int) -> None:
            if q and q[0] == i-k:
                q.popleft()
            
            while q and nums[i] > nums[q[-1]]:
                q.pop()
        
        for i in range(k):
            cleanFor(i)
            q.append(i)

        res = []
        for i in range(n):
            cleanFor(i)
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res

s = Solution()
print(s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
