class Solution:
    # [1,1,2,3,7]
    # [9,9,9,9]
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        arr.sort()
        res = 1
        for i in range(1, len(arr)):
            if arr[i] > res:
                res += 1
        return res

    def counting(self, arr: list[int]) -> int:
        n = len(arr)
        counter = [0] * (n + 1)
        for v in arr:
            counter[min(v, n)] += 1
        res = 1
        for i in range(2, n + 1):
            res = min(res + counter[i - 1], i)
        return res
            
        
        