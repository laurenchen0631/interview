class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        res: list[str] = []
        for q in queries:
            # In one edit you can take a word from queries, and change any letter in it to any other letter.
            for word in dictionary:
                if len(word) != len(q):
                    continue
                if sum(1 for a, b in zip(word, q) if a != b) <= 2:
                    res.append(q)
                    break
        return res

s = Solution()
print(s.twoEditWords(queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]))
print(s.twoEditWords(queries = ["yes"], dictionary = ["not"]))