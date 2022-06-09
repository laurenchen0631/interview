class Solution:
    def minSwaps(self, data: list[int]) -> int:
        n = 0
        for e in data:
            if e == 1:
                n += 1
        
        maxSection = window = sum(data[:n])
        for i in range(1, len(data)-n+1):
            if data[i-1] == 1:
                window -= 1
            if data[i+n-1]:
                window += 1
            maxSection = max(maxSection, window)
        return n - maxSection

s = Solution()
print(s.minSwaps([1,0,1,0,1]))
print(s.minSwaps([0,0,1,0,0]))
print(s.minSwaps([1,0,1,0,1,0,0,1,1,0,1]))