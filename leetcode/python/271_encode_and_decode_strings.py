class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        for s in strs:
            res.append(f"{len(s)}@{s}")
        return ''.join(res)
        

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '@':
                j += 1
            l = int(s[i:j])
            res.append(s[j+1:j+1+l])
            i = j + 1 + l
        return res
        

