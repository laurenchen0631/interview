import math

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if not set(target) <= set(source):
            return -1
        i = 0
        for c in target:
            while c != source[i % len(source)]:
                i += 1
            i += 1
        return math.ceil(i / len(source))

s = Solution()
print(s.shortestWay(source = "abc", target = "abcbc"))
print(s.shortestWay(source = "abc", target = "acdbc"))
print(s.shortestWay(source = "xyz", target = "xzyxz"))
print(s.shortestWay("abcd", "ab"))
print(s.shortestWay("mdnlyhouuvygqloafgratkduqidlcomugwjtnqlwnmligxdfdawjhqyimbamjougclvaiclpgvorxrstaefbnylcqm", "tyuzcctqqnofrybyiickshnqnsqmitzcwxpcdjrcjbyviugwwyjvvxnevqrlfiorxudvlebveeovfbogeupbibqwex"))

