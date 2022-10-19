from collections import defaultdict
from email.policy import default


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        graph, incoming = self.buildGraph(words)
        if graph is None:
            return ""
        return self.topoTraverse(graph, incoming)

    def buildGraph(self, words: list[str]) -> tuple[dict[str, set[str]], dict[str, int]] | tuple[None, None]:
        graph = defaultdict(set)
        incoming = {c: 0 for c in set("".join(words))}
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        incoming[c2] += 1
                    break
            else: # prefix of w1 is w2 but w1 is longer
                if len(w1) > len(w2):
                    return None, None
        return graph, incoming

    def topoTraverse(self, graph: dict[str, set[str]], incoming: dict[str, int]) -> str:
        queue = [c for c in incoming if incoming[c] == 0]
        res = []
        while queue:
            c = queue.pop()
            res.append(c)
            for n in graph[c]:
                incoming[n] -= 1
                if incoming[n] == 0:
                    queue.append(n)
        return "".join(res) if len(res) == len(incoming) else ""
        
s = Solution()
print(s.alienOrder(["wrt","wrf","er","ett","rftt"]))
# print(s.alienOrder(["z", "x", "z"]))
# print(s.alienOrder(["abc","ab"]))