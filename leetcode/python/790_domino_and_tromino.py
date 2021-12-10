class Solution:
    def __init__(self) -> None:
        self.mod = 10 ** 9 + 7

    def numTilings(self, n: int) -> int:
        f: list[int] = [0, 1, 2] + [0] * (n - 2)
        p: list[int] = [0, 0, 1] + [0] * (n - 2)
        for k in range(3, n+1):
            f[k] = (f[k-1] + f[k-2] + 2*p[k-1]) % self.mod
            p[k] = p[k-1] + f[k-2]
        return f[n]

if __name__ == '__main__':
  s = Solution()
  print(s.numTilings(3))
  print(s.numTilings(4))
  print(s.numTilings(5))