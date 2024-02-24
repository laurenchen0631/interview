from collections import defaultdict


class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))
            
        earliest = [100001] * n
        earliest[0] = 0
        earliest[firstPerson] = 0
        
        stack = [(0, 0), (firstPerson, 0)]
        while stack:
            person, time = stack.pop()
            for t, next_person in graph[person]:
                if t >= time and earliest[next_person] > t:
                    earliest[next_person] = t
                    stack.append((next_person, t))
        
        return [i for i in range(n) if earliest[i] != 100001]
         