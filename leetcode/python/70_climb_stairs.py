class Solution:
    def __init__(self):
        self.cache: dict[int, int] = {
            1: 1,
            2: 2
        }

    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        
        self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.cache[n]

    def climbStarsAlt(self, n: int) -> int:
        dp = [1, 2]
        if n < 3:
            return dp[n-1]
        for _ in range(3, n+1):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(1))
    print(s.climbStairs(3))
    print(s.climbStairs(4))
    print(s.climbStarsAlt(1))
    print(s.climbStarsAlt(3))
    print(s.climbStarsAlt(4))