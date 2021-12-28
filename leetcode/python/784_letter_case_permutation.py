class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        res: list[str] = []
        self.helper(0, list(s), res)
        return res
    
    def helper(self, index: int, s: list[str], res: list[str]):
        if index == len(s):
            return res.append(''.join(s))

        if not s[index].isalpha():
            self.helper(index+1, s, res)
        else:
            s[index] = s[index].lower()
            self.helper(index+1, s, res)
            s[index] = s[index].upper()
            self.helper(index+1, s, res)


if __name__ == '__main__':
    s = Solution()
    print(s.letterCasePermutation('a1b2'))
    print(s.letterCasePermutation('3z4'))
    print(s.letterCasePermutation('C'))