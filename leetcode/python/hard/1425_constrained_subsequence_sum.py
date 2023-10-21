import heapq


class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        heap = [(-nums[0], 0)]
        res = nums[0]
        
        for i in range(1, len(nums)):
            while heap and heap[0][1] < i - k:
                heapq.heappop(heap)
            
            cur = max(0, -heap[0][0]) + nums[i]
            res = max(res, cur)
            heapq.heappush(heap, (-cur, i))
        return res
        