class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        for i in range(0, len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                res = max(res, num[i])
        return res * 3
            
        