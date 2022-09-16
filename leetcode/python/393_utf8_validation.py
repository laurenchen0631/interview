class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        i: int = 0
        while i < len(data):
            n = self.getNumBytes(data[i])
            if not n or (n == 1 and data[i] >> 7) or i + n > len(data):
                return False
            for j in range(i + 1, i + n):
                if data[j] >> 6 != 0b10:
                    return False
            i += n
        return True
    
    def getNumBytes(self, n: int) -> int:
        if (n >> 3) == 0b11110:
            return 4
        elif (n >> 4) == 0b1110:
            return 3
        elif (n >> 5) == 0b110:
            return 2
        elif (n >> 7) == 0:
            return 1
        else:
            return 0
        
s = Solution()
print(s.validUtf8([197,130,1]))
print(s.validUtf8([235,140,4]))