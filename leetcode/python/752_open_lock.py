class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if target in deadends: return -1
        if '0000' in deadends: return -1
        queue = deque(['0000'])
        level = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == target:
                    return level
                for i in range(4):
                    pre = node[:i]
                    post = node[i + 1:]
                    for op in [-1,1]:
                        nxt = pre + str((int(node[i]) + op) % 10) + post
                        if nxt not in deadends:
                            deadends.add(nxt)
                            queue.append(nxt)
            level += 1
        return -1
