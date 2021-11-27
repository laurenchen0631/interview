class Solution:
  def findNumbers(self, nums: list[int]) -> int:
    res = 0
    for n in nums:
      print(n, self.getDigits(n))
      if self.isEven(self.getDigits(n)):
        res += 1
    return res

  def findNumbersOpt(self, nums: list[int]) -> int:
    count = 0
    for num in nums:
      if self.isEven(len(str(num))):
          count +=1
    return count

  def isEven(self, n: int) -> bool:
    return n & 1 == 0

  def getDigits(self, n: int) -> int:
    digits = 0
    while n != 0:
      n //= 10
      digits += 1
    return digits
    
if __name__ == '__main__':
  s = Solution()
  print(s.findNumbers([12,345,2,6,7896]))
  print(s.findNumbers([555,901,482,1771]))