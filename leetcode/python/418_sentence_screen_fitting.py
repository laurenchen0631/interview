class Solution:
    def wordsTyping(self, sentence: list[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence) + ' '
        dp = [0] * len(s)
        for i in range(1, len(s)):
            dp[i] = dp[i-1] - 1 if s[i] != ' ' else 1
        count: int = 0
        for _ in range(rows):
            count += cols
            count += dp[count % len(s)]
        return count // len(s)

s = Solution()
print(s.wordsTyping(sentence = ["hello","world"], rows = 2, cols = 8))
print(s.wordsTyping(["a", "bcd", "e"], rows = 3, cols = 6))
print(s.wordsTyping(["i","had","apple","pie"], rows = 4, cols = 5))