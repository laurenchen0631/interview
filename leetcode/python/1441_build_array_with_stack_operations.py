class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        res: list[str] = []
        i = 0
        for k in range(1, n+1):
            if k == target[i]:
                res.append("Push")
                i += 1
            else:
                res.append("Push")
                res.append("Pop")
            if i == len(target):
                break
        return res