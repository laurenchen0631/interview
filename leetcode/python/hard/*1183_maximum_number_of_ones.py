class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        count = []
        # count the number of squares related with (i, j)
        for i in range(sideLength):
            for j in range(sideLength):
                num = (1 + (width - j - 1) // sideLength) * (1 + (height - i - 1) // sideLength)
                count.append(num)
        count.sort(reverse=True)
        return sum(count[:maxOnes])