class Solution:
    def killProcess(self, pid: list[int], ppid: list[int], kill: int) -> list[int]:
        kills = set([kill])
        visited = set([0])
        parent = {pid[i]: ppid[i] for i in range(len(pid))}
        def dfs(p: int, path: list[int]) -> None:
            if p in kills:
                return kills.update(path)
            if p in visited:
                return visited.update(path)
            path.append(p)
            dfs(parent[p], path)
        for p in pid:
            if p not in visited and p not in kills:
                dfs(p, [])
        return list(kills)

s = Solution()
print(s.killProcess(pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5))
print(s.killProcess(pid = [1], ppid = [0], kill = 1))