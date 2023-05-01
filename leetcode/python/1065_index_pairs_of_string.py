class Solution:
    def indexPairs(self, text: str, words: list[str]) -> list[list[int]]:
        trie = self.buildTrie(words)
        res: list[list[int]] = []
        for i in range(len(text)):
            node = trie
            for j in range(i, len(text)):
                if text[j] not in node:
                    break
                node = node[text[j]]
                if '#' in node:
                    res.append([i, j])
        return res
    
    def buildTrie(self, words: list[str]) -> dict:
        trie = {}
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['#'] = True
        return trie