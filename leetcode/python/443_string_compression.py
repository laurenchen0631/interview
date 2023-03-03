class Solution:
    def compress(self, chars: list[str]) -> int:
        l = r = 0
        while r < len(chars):
            c = chars[r]
            count = 1
            r += 1
            while r < len(chars) and chars[r] == c:
                count += 1
                r += 1
            chars[l] = c
            l += 1
            if count > 1:
                for d in str(count):
                    chars[l] = d
                    l += 1
        return l
    
    