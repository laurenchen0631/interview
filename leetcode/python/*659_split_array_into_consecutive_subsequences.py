import heapq


class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        subseqs: list[tuple[int, int]] = []
        for n in nums:
            while subseqs and subseqs[0][0] + 1 < n:
                seq = heapq.heappop(subseqs)
                if seq[1] < 3:
                    return False
            if not subseqs or subseqs[0][0] == n:
                heapq.heappush(subseqs, (n, 1))
            else:
                seq = heapq.heappop(subseqs)
                heapq.heappush(subseqs, (n, seq[1] + 1))
            print(subseqs)
            
        
        for seq in subseqs:
            if seq[1] < 3:
                return False
        return True

s = Solution()
print(s.isPossible([1,2,3,3,4,5]))
# print(s.isPossible([1,2,3,3,4,4,5,5]))
# print(s.isPossible([1,2,3,4,4,5,5]))
        