class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        cross = {(1, 3): 2, (1, 7): 4, (1, 9): 5, (2, 8): 5, (3, 7): 5, (3, 9): 6, (4, 6): 5, (7, 9): 8, 
                 (3, 1): 2, (7, 1): 4, (9, 1): 5, (8, 2): 5, (7, 3): 5, (9, 3): 6, (6, 4): 5, (9, 7): 8}
        seen = set[int]()
        ways = 0
        def getValidKeys(last, seen):
            nonlocal ways
            if len(seen) > n:
                return
            elif len(seen) >= m:
                ways += 1 
            for number in range(1, 10):
                if number in seen:
                    continue
                if (last, number) not in cross or cross[(last, number)] in seen:
                    seen.add(number)
                    getValidKeys(number, seen)
                    seen.remove(number)
        
        getValidKeys(0, seen)
        
        return ways

s = Solution()
print(s.numberOfPatterns(m = 1, n = 1))
print(s.numberOfPatterns(m = 1, n = 2))