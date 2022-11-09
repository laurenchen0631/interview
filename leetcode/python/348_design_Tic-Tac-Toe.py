class TicTacToe:
    def __init__(self, n: int):
        self._n = n
        self._rows = [[set[int](), 0] for _ in range(n)]
        self._cols = [[set[int](), 0] for _ in range(n)]
        self._diag = [[set[int](), 0], [set[int](), 0]]

    def move(self, row: int, col: int, player: int) -> int:
        if self._check(self._rows[row], player):
            return player
        if self._check(self._cols[col], player):
            return player
        if row - col == 0 and self._check(self._diag[0], player):
            return player
        if row + col == self._n - 1 and self._check(self._diag[1], player):
            return player
        return 0

    def _check(self, cache: list, player: int) -> int:
        cache[0].add(player)
        cache[1] += 1
        if cache[1] == self._n and len(cache[0]) == 1:
            return True
        return False
