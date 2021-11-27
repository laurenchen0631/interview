class Solution:
  def findOccurrences(self, text: str, first: str, second: str) -> list[str]:
    words = text.split(' ')
    result: list[str] = []
    for i in range(len(words) - 2):
      if words[i] == first and words[i+1] == second:
        result.append(words[i+2])
    return result        

if __name__ == '__main__':
  s = Solution()
  print(s.findOccurrences("alice is a good girl she is a good student", "a", "good"))
  print(s.findOccurrences("we will we will rock you", "we", "will"))
  print(s.findOccurrences("we we we we we", "we", "we"))
  