class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        visited1 = set[int]()
        visited2 = set[int]()
        while node1 != -1 or node2 != -1:
            res = []
            if node1 != -1:
                if node1 in visited2:
                    res.append(node1)
                visited1.add(node1)
                node1 = edges[node1]
                if node1 in visited1:
                    node1 = -1
            if node2 != -1 and node2 not in visited2:
                if node2 in visited1:
                    res.append(node2)
                visited2.add(node2)
                node2 = edges[node2]
                if node2 in visited2:
                    node2 = -1
            if res:
                return min(res)
        return -1
    
s = Solution()
print(s.closestMeetingNode(edges = [2,2,3,-1], node1 = 0, node2 = 1))
print(s.closestMeetingNode(edges = [1,2,-1], node1 = 0, node2 = 2))
print(s.closestMeetingNode([5,4,5,4,3,6,-1], node1 = 0, node2 = 1))
print(s.closestMeetingNode([4,4,8,-1,9,8,4,4,1,1], node1 = 5, node2 = 6))