from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        courses: list[set[int]] = [set() for _ in range(numCourses)]
        for p in prerequisites:
            courses[p[0]].add(p[1])
        
        availables = set[int]()
        for i, course in enumerate(courses):
            if len(course) == 0:
                availables.add(i)
        
        res: list[int] = []
        while len(availables) > 0:
            res.extend(availables)
            tmp = set[int]()
            for i, course in enumerate(courses):
                if len(course) == 0:
                    continue
                
                courses[i] = course.difference(availables)
                if len(courses[i]) == 0:
                    tmp.add(i)
            availables = tmp

        if len(res) != numCourses:
            return []

        return res

    def findOrderOpt(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        degree = [0 for _ in range(numCourses)]
        courses = [[] for _ in range(numCourses)]
        
        for (in_node, out_node) in prerequisites:
            degree[in_node] += 1
            courses[out_node].append(in_node)
            
        que = deque()
        results = []
        cnt = 0
        for i in range(len(degree)):
            if degree[i] == 0:
                que.append(i)
                
        while que:
            node = que.popleft()
            cnt += 1
            results.append(node)
            
            for next_course in courses[node]:
                degree[next_course] -= 1
                if degree[next_course] == 0:
                    que.append(next_course)
        if cnt == numCourses:
            return results
        return []
                

if __name__ == '__main__':
    s = Solution()
    # print(s.findOrder(2, [[1,0]]))
    # print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    # print(s.findOrder(1, []))
    print(s.findOrder(3, [[1,0],[1,2],[0,1]]))
