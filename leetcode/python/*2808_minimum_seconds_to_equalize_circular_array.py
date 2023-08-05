class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        dic = defaultdict(list)
        for i, num in enumerate(nums):
            dic[num].append(i)
        if len(dic) == 1:
            return 0
        res = float('inf')
        for v in dic.values():
            v.append(v[0] + n)
            diff = [v[i] - v[i-1] for i in range(1, len(v))]
            res = min(res, max(diff) // 2)
        return res