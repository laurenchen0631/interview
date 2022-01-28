class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        lookup = self.trie
        for c in word:
            if c not in lookup:
                lookup[c] = {}
            lookup = lookup[c]
        lookup['#'] = True
        print(self.trie)

    def search(self, word: str) -> bool:
        return self.searchImpl(0, word, self.trie)

    def searchImpl(self, index: int, word: str, lookup: dict) -> bool:
        if index == len(word):
            return '#' in lookup
        
        c = word[index]
        if c != '.':
            if c not in lookup:
                return False
            if self.searchImpl(index+1, word, lookup[c]):
                return True
        else:
            for key in lookup.keys():
                if key != '#' and self.searchImpl(index+1, word, lookup[key]):
                    return True
        return False


# obj = WordDictionary()
# obj.addWord('bad')
# obj.addWord('dad')
# obj.addWord('mad')
# print(obj.search('pad'))
# print(obj.search('bad'))
# print(obj.search('b..'))
# print(obj.search('.ad'))


w = WordDictionary()
w.addWord('a')
w.addWord('a')
# print(w.search('.'))
# print(w.search('a'))
# print(w.search('aa'))
# print(w.search('a'))
# print(w.search('.a'))
print(w.search('a.'))
