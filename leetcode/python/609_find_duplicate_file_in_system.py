from collections import defaultdict
import re

class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        duplicates = defaultdict[str](list[str])
        for path in paths:
            parts = path.split()
            for f in parts[1:]:
                m = re.match('(.+)\((.+)\)', f)
                duplicates[m.group(2)].append(parts[0] + '/' + m.group(1))
        res: list[list[str]] = []
        for content in duplicates:
            if len(duplicates[content]) > 1:
                res.append(duplicates[content])
        return res

s = Solution()
print(s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))