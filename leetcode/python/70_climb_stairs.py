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


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(1))
    print(s.climbStairs(3))
    print(s.climbStairs(4))