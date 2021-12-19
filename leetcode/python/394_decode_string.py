class Solution:
    def decodeString(self, s: str) -> str:
        self.index = 0
        return self.helper(s)

    def helper(self, s: str) -> str:
        res: str = ''
        while self.index < len(s) and s[self.index] != ']':
            if not s[self.index].isdigit():
                res += s[self.index]
                self.index += 1
            else:
                k: int = 0
                while s[self.index].isdigit():
                    k = 10 * k + int(s[self.index])
                    self.index += 1
                self.index += 1 # [
                nested = self.helper(s)
                self.index += 1 # ]
                res += k * nested
        return res
    
if __name__ == '__main__':
  s = Solution()
  print(s.decodeString('2[abc]3[cd]ef'))
  print(s.decodeString('3[a2[c]]'))