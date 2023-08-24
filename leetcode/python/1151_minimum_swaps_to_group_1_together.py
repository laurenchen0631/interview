class Solution:
    def minSwaps(self, data: list[int]) -> int:
        k = data.count(1)
        cur_max_ones = 0
        cur_count = data[:k].count(1)
        for i, n in enumerate(data[k:]):
            cur_max_ones = max(cur_max_ones, cur_count)
            if n == 1:
                cur_count += 1
            if data[i] == 1:
                cur_count -= 1
        return k - max(cur_max_ones, cur_count)
        
        
        