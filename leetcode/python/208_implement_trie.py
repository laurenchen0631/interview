class Trie:
    def __init__(self):
        self._trie = {}

    def insert(self, word: str) -> None:
        cur = self._trie
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True
        

    def search(self, word: str) -> bool:
        cur = self._trie
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return '#' in cur
        

    def startsWith(self, prefix: str) -> bool:
        cur = self._trie
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True
        

obj = Trie()
obj.insert("apple")
obj.search("apple")
obj.search("app")
obj.startsWith("app")
obj.startsWith("app")
obj.search("app")