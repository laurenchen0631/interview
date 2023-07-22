import re


class Solution:
    def sortVowels(self, s: str) -> str:
        voewls = set('aeiouAEIOU')
        bucket = []
        for c in s:
            if c in voewls:
                bucket.append(c)
        bucket.sort(reverse=True)
        res = []
        
        for c in s:
            if c in voewls:
                res.append(bucket.pop())
            else:
                res.append(c)
        return ''.join(res)
        