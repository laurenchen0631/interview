class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n, key=lambda x: ord(x)))

s = Solution()
print(s.minPartitions("32"))
print(s.minPartitions("82734"))
print(s.minPartitions("27346209830709182346"))