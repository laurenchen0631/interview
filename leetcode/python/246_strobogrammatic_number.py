class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotatedNum = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6",
        }
        for i in range((len(num) + 1) // 2):
            d = num[i]
            if d not in rotatedNum:
                return False
            if rotatedNum[d] != num[-1 - i]:
                return False
        return True
    
s = Solution()
print(s.isStrobogrammatic("69"))
print(s.isStrobogrammatic("818"))
print(s.isStrobogrammatic("1234"))