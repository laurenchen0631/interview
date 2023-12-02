from collections import Counter


class Solution:
    # words = ["cat","bt","hat","tree"], chars = "atach"
    def countCharacters(self, words: list[str], chars: str) -> int:
        usable = Counter(chars)
        res = 0
        for w in words:
            count = Counter(w)
            flag = True
            for k, v in count.items():
                if k not in usable or usable[k] < v:
                    flag = False
                    break
            if flag:
                res += len(w)
        return res
        