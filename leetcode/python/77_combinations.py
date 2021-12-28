class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res: list[list[int]] = []
        self.helper(1, n, k, [], res)
        return res
    
    def helper(self, low: int, high: int, k: int, pair: list[int], res: list[list[int]]) -> None:
        if k == 0:
            res.append(pair.copy())
            return
        
        for i in range(low, high + 2 - k):
            pair.append(i)
            self.helper(i+1, high, k-1, pair, res)
            pair.pop()

if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
    print(s.combine(1, 1))
    print(s.combine(6, 4))