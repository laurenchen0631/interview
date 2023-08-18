class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        count = [0] * n
        roads_set = set()
        for i, j in roads:
            count[i] += 1
            count[j] += 1
            roads_set.add((i, j))
            roads_set.add((j, i))
            
        max_rank = 0
        for i in range(n):
            for j in range(i+1, n):
                rank = count[i] + count[j]
                if (i, j) in roads_set:
                    rank -= 1
                max_rank = max(max_rank, rank)
        return max_rank