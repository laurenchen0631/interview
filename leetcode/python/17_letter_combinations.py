class Solution:
    def __init__(self):
        self.keyboard: dict[str, list[str]] = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []

        res: list[str] = []
        self.helper(digits, 0, [], res)
        return res
    
    def helper(self, digits: str, index: int, letters: list[str], res: list[str]):
        if index == len(digits):
            return res.append(''.join(letters))
        
        chars = self.keyboard[digits[index]]
        for c in chars:
            letters.append(c)
            self.helper(digits, index+1, letters, res)
            letters.pop()

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
    print(s.letterCombinations(''))
    print(s.letterCombinations('2'))
    print(s.letterCombinations('345'))