class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]):
        root = self.find_root(leftChild, rightChild)
        if root is None:
            return False

        visited = set()
        q = [root]
        while q:
            node = q.pop()
            if node in visited:
                return False
            visited.add(node)
            if leftChild[node] != -1:
                q.append(leftChild[node])
            if rightChild[node] != -1:
                q.append(rightChild[node])
                
        return len(visited) == n
        
    def find_root(self, leftChild: list[int], rightChild: list[int]) -> int | None:
        n = len(leftChild)
        nodes = set(range(n))
        for i in range(n):
            if leftChild[i] in nodes:
                nodes.remove(leftChild[i])
            if rightChild[i] in nodes:
                nodes.remove(rightChild[i])
                
        if len(nodes) == 1:
            return nodes.pop()
        else:
            return None
        
        
        