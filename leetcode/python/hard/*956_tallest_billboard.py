class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        dp = {0: 0} # diff: shorter height
        for h in rods:
            for diff, v in list(dp.items()):
                # add to taller
                dp[diff + h] = max(dp.get(diff + h, 0), v)
                
                # add to shorter
                dp[abs(diff - h)] = max(dp.get(abs(diff - h), 0), v + min(diff, h))
        return dp[0]