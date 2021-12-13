import math

class Solution:
    def __init__(self) -> None:
        self.mod = 10**9 + 7

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lcd = a * b // math.gcd(a, b)
        group = (lcd//a) + (lcd//b) - 1
        k, i = divmod(n, group)

        heads = [0, 0]
        for i in range(i + 1):
            if heads[0] <= heads[1]:
                heads[0] += a
            else:
                heads[1] += b

        return (lcd * int(k) + min(heads)) % self.mod


if __name__ == '__main__':
  s = Solution()
  print(s.nthMagicalNumber(1, 2, 3))
  print(s.nthMagicalNumber(4, 2, 3))
  print(s.nthMagicalNumber(5, 2, 4))
  print(s.nthMagicalNumber(3, 6, 4))