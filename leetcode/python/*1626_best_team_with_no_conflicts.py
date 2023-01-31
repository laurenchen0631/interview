class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        players = sorted(zip(ages, scores))
        n = len(players)
        dp = [0] * n
        res = 0
        for i in range(n):
            dp[i] = players[i][1]
            for j in range(i-1, -1, -1):
                if players[i][1] >= players[j][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
            res = max(res, dp[i])
        return res