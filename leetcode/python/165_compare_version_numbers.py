class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i1 = i2 = 0
        while i1 < len(version1) or i2 < len(version2):
            e1 = i1
            while e1 < len(version1) and version1[e1] != '.':
                e1 += 1
            e2 = i2
            while e2 < len(version2) and version2[e2] != '.':
                e2 += 1
            p1 = int(version1[i1:e1]) if i1 < e1 else 0
            p2 = int(version2[i2:e2]) if i2 < e2 else 0
            if p1 < p2:
                return -1
            elif p1 > p2:
                return 1
            i1 = e1+1
            i2 = e2+1
        return 0

s = Solution()
print(s.compareVersion(version1 = "1.01", version2 = "1.001"))
print(s.compareVersion(version1 = "1.0", version2 = "1.0.0"))
print(s.compareVersion(version1 = "1.0", version2 = "1.0.1"))
print(s.compareVersion(version1 = "0.1", version2 = "1.1"))