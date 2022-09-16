from collections import Counter


class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        counter = Counter(changed);
        changed.sort()
        res: list[int] = []
        for n in changed:
            if counter[n] == 0:
                continue
            counter[n] -= 1
            if (k := n * 2) in counter and counter[k] > 0:
                counter[k] -= 1
                res.append(n)
            else:
                return []
        return res

s = Solution()
print(s.findOriginalArray([1,3,4,2,6,8]))
print(s.findOriginalArray([1,0,4,2,8,0]))
print(s.findOriginalArray([12,8,4,6,2,4,8,16]))
print(s.findOriginalArray([6,3,0,1]))
print(s.findOriginalArray([0,0,0,0]))

