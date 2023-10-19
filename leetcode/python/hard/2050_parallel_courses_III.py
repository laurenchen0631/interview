class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        g, incoming = self.build_graph(n, relations)
        max_incoming = { i: 0 for i in range(n) }
        cur = 0
        topo = [i for i in range(n) if incoming[i] == 0]
        while topo:
            tmp = []
            for course in topo:
                t = time[course] + max_incoming[course]
                for next_course in g[course]:
                    incoming[next_course] -= 1
                    max_incoming[next_course] = max(max_incoming[next_course], t)
                    if incoming[next_course] == 0:
                        tmp.append(next_course)
                cur = max(cur, t)
            topo = tmp
        return cur
        
    def build_graph(self, n: int, relations: list[list[int]]) -> tuple[dict[int, list[int]], dict[int, int]]:
        g = { i: [] for i in range(n) }
        incoming = { i: 0 for i in range(n)}
        for u, v in relations:
            g[u-1].append(v-1)
            incoming[v-1] += 1
            
        return g, incoming