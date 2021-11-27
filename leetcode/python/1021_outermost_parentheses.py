class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        phrase: list[str] = []
        left: int = 0

        for c in s:
            if c == '(':
                if left > 0:
                    phrase.append(c)
                left += 1
            else:
                left -= 1
                if left > 0:
                    phrase.append(c)

        return ''.join(phrase)
                

if __name__ == '__main__':
  s = Solution()
  print(s.removeOuterParentheses("(()())(())"))
  print(s.removeOuterParentheses("(()())(())(()(()))"))
  print(s.removeOuterParentheses("()()"))