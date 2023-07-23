# import heapq

class Solution:
    def maxIncreasingGroups(self, usageLimits: list[int]) -> int:
        # heap = [(-limit, i) for i, limit in enumerate(usageLimits)]
        # for i in range(1, len(usageLimits) + 1):
        #     if len(heap) < i:
        #         return i - 1

        #     heapq.heapify(heap)
        #     used = []
        #     for _ in range(i):
        #         limit, index = heapq.heappop(heap)
        #         if limit < -1:
        #             used.append((limit + 1, index))
        #     heap.extend(used)
        # return len(usageLimits)
        
        usageLimits.sort()
        total, count = 0, 0
        for limit in usageLimits:
            total += limit
            if total >= ((count+1)*(count+2))//2: # to form k groups we need k*(k+1)/2 numbers
                count += 1
                
        return count
        

s = Solution()

# print(s.maxIncreasingGroups([1,2,5]))
# print(s.maxIncreasingGroups([2,1,2]))
# print(s.maxIncreasingGroups([1,1]))
print(s.maxIncreasingGroups([1,1,1,4]))
print(s.maxIncreasingGroups([1,1,1,1,1,1,1,1,1,1,]))