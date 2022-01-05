class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        visited = set[int]()
        count: int = 0
        for i in range(len(isConnected)):
            if i in visited:
                continue
            
            count += 1
            q: list[int] = [i]
            while q:
                p = q.pop()
                if p in visited:
                    continue
                visited.add(p)
                for j, link in enumerate(isConnected[p]):
                    if link == 1:
                        q.append(j)
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
    print(s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
