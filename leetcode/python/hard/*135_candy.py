class Solution:
    # [12, 4, 3, 11, 34, 34, 1, 67]
    def candy(self, ratings: list [int]) -> int:
        n = len(ratings)
        left = [1] * n #  [1, 1, 1, 2, 3, 1, 1, 2]
        right = [1] * n # [3, 2, 1, 1, 1, 2, 1, 1]
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i]= right[i+1] + 1
        
        return sum([max(l, r) for l, r in zip(left, right)])