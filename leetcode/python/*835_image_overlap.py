
class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        original: list[list[tuple[int, int]]] = []
        translated: list[list[tuple[int, int]]] = []
        n = len(img1)

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    original.append((i, j))
                if img2[i][j] == 1:
                    translated.append((i, j))
        
        translations = dict[tuple[int, int], int]()
        res = 0
        for (i, j) in translated:
            for (x, y) in original:
                translation = (i - x, j - y)
                translations[translation] = translations.get(translation, 0) + 1
                res = max(res, translations[translation])
        return res

s = Solution()
print(s.largestOverlap(img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]))