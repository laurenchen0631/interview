class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0
        for length in range(1, k+1):
            remainder = (remainder*10+1) % k
            if remainder == 0:
                return length
        return -1

if __name__ == '__main__':
  s = Solution()
  print(s.smallestRepunitDivByK(1))
  print(s.smallestRepunitDivByK(3))
  print(s.smallestRepunitDivByK(7))
  print(s.smallestRepunitDivByK(9))
  print(s.smallestRepunitDivByK(11))
  print(s.smallestRepunitDivByK(13))