import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        n = len(beginWord)
        comboDict = collections.defaultdict(list)
        for word in wordList:
            for i in range(n):
                comboDict[word[:i] + "*" + word[i+1:]].append(word)

        # Queue for BFS
        queue = collections.deque([(beginWord, 1)]) # (word, level)
        visited = set([beginWord])
        while queue:
            current_word, level = queue.popleft()
            for i in range(n):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                for word in comboDict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
                comboDict[intermediate_word] = []
        return 0

s = Solution()
print(s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
print(s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))