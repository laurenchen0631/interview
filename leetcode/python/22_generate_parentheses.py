class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res: list[str] = []
        self.helper(n, 0, 0, [], res)
        return res
    
    def helper(self, n: int, left: int, right: int, comb: list[str], res: list[str]):
        if len(comb) == 2 * n:
            return res.append(''.join(comb))
        
        if left < n:
            comb.append('(')
            self.helper(n, left + 1, right, comb, res)
            comb.pop()
        if right < left:
            comb.append(')')
            self.helper(n, left, right + 1, comb, res)
            comb.pop()

if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
    print(s.generateParenthesis(2))
    print(s.generateParenthesis(1))
    print(s.generateParenthesis(4))