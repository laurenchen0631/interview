class Solution:
    def __init__(self) -> None:
        self.codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        transformation = set[str]()
        for w in words:
            transformation.add(''.join(self.codes[ord(c) - ord('a')] for c in w))
        return len(transformation)

s = Solution()
print(s.uniqueMorseRepresentations(words = ["gin", "zen", "gig", "msg"]))