class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = 0
        chars = list(s)
        while right < len(s):
          if s[right] == ' ':
            self.reverse(chars, left, right-1)
            left = right + 1
          right += 1
        self.reverse(chars, left, right-1)
        return ''.join(chars)

    def reverse(self, s: list[str], l: int, r: int):
      while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    def reverseWordsShort(self, s: str) -> str:
      chars = list(s)
      chars.reverse()
      words = ''.join(chars).split()
      words.reverse()

      return ' '.join(words)

if __name__ == '__main__':
  s = Solution()
  print(s.reverseWords("Let's take LeetCode contest"))
  print(s.reverseWordsShort("Let's take LeetCode contest"))
  print(s.reverseWords("God Ding"))
  print(s.reverseWords("Dog"))