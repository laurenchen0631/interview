class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low = low + 1 if low & 1 == 0 else low
        high = high - 1 if high & 1 == 0 else high
        return (high - low) // 2 + 1