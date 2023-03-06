class Solution:
    def validWordSquare(self, words: list[str]) -> bool:
        m = len(words)
        n = max(len(word) for word in words)
        if m != n or n != len(words[0]):
            return False
        
        for j in range(n):
            w = []
            for i in range(m):
                if j < len(words[i]):
                    w.append(words[i][j])
            if words[j] != ''.join(w):
                return False
        return True
                