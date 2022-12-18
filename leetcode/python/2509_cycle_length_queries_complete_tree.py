class Solution:
    def cycleLengthQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        ans = []
        for p, q in queries:
            path = 0
            while p != q:
                path += 1
                if p > q:
                    p >>= 1
                else:
                    q >>= 1
            ans.append(path + 1) # to account for path between p and q
        return ans
            
s = Solution()
print(s.cycleLengthQueries(5, [[23,5],[15,7],[3,21],[31,9],[5,15],[11,2],[19,7]]))