class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        postfix = {0: 0}
        cur = 0
        res = n + 1
        for i in range(n - 1, -1, -1):
            cur += nums[i]
            postfix[cur] = n - i
            if cur == x:
                res = min(res, n - i)
        
        cur = 0
        for i in range(n):
            cur += nums[i]
            complement = x - cur
            if complement in postfix:
                res = min(res, postfix[complement] + i + 1)
        return res if res <= n else -1