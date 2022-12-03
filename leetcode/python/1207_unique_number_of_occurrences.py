from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occurrence = Counter(arr)
        return len(occurrence) == len(set(occurrence.values()))
        
s = Solution()
print(s.uniqueOccurrences([1,2,2,1,1,3]))
print(s.uniqueOccurrences([1,2]))