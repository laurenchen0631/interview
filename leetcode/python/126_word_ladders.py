from collections import defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        n = len(beginWord)
        comboDict = defaultdict(list[str])
        wordSet = set(wordList)
        for word in wordList:
            for i in range(n):
                comboDict[word[:i] + "*" + word[i+1:]].append(word)
        layer = {beginWord: [[beginWord]]}
        while layer:
            tmp = defaultdict(list[list[str]])
            for word in layer:
                if word == endWord:
                    return layer[word]

                for i in range(n):
                    intermediate_word = word[:i] + "*" + word[i+1:]
                    for w in comboDict[intermediate_word]:
                        if w in wordSet:
                            tmp[w] += [ladder + [w] for ladder in layer[word]]
            wordSet -= set(tmp.keys())
            layer = tmp
        return []
    
    def findLaddersOpt(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        # edge case
        if endWord not in wordList:
            return []
        
        # 1) build neighbor list for first bfs
        if beginWord not in wordList:
            wordList.append(beginWord)
        unvisited = set(wordList)
        n = len(beginWord)
        neighbors = defaultdict(list)
        for word in wordList:
            for i in range(n):
                neighbors[f'{word[:i]}*{word[i+1:]}'].append(word)
        
        # 2) do first bfs and build reversed neighbors list for second bfs
        reverseNeighbors = defaultdict(list)
        stack = [beginWord]
        unvisited.remove(beginWord)
        while stack:
            visited = set()
            for word in stack:
                for i in range(n):
                    for neighbor in neighbors[f'{word[:i]}*{word[i+1:]}']:
                        if neighbor in unvisited:
                            reverseNeighbors[neighbor].append(word)
                            visited.add(neighbor)
            stack = list(visited)
            unvisited -= visited
            if reverseNeighbors[endWord]:
                break
        
        # if endWord does not have reversed neigbors it is not reachable so return empty list
        if not reverseNeighbors[endWord]:
            return []
        
        # 3) do second bfs
        paths = [[endWord]]
        while True:
            ladder = []
            for path in paths:
                last_node = path[-1]
                for reverse_neighbor in reverseNeighbors[last_node]:
                    ladder.append(path + [reverse_neighbor])
            paths = ladder
            if paths[0][-1] == beginWord:
                break
        
        # 4) reverse the paths
        result = []
        for path in paths:
            path.reverse()
            result.append(path)
        return result

s = Solution()
print(s.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
print(s.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))