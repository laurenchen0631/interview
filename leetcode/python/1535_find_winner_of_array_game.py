class Solution:
    # arr = [2,1,3,5,4,6,7], k = 2 -> 5, [3, 5, 4]
    # arr = [2,1,3,5,4,6,7], k = 3 -> 
    # [2, 3, 5, 4, 6, 7, 1]
    # [3, 5, 4, 6, 7, 1, 2]
    # [5, 4, 6, 7, 1, 2, 3]
    # [5, 6, 7, 1, 2, 3, 4]
    # [6, 7, 1, 2, 3, 4, 5]
    # [7, 1, 2, 3, 4, 5, 6]

    # arr = [5, 3, 4, 7, 1, 8]
    # arr = [5, 4, 7, 1, 8, 3]
    # arr = [5, 7, 1, 8, 3, 4]
    # arr = [7, 1, 8, 3, 4, 5]
    # arr = [7, 8, 3, 4, 5, 1]
    # arr = [8, 3, 4, 5, 1, 7]

    def getWinner(self, arr: list[int], k: int) -> int:
        cur_winner = arr[0]
        wins = 0
        for n in arr[1:]:
            if cur_winner < n:
                cur_winner = n
                wins = 1
            else:
                wins += 1
            if wins == k:
                return cur_winner
        return cur_winner
        