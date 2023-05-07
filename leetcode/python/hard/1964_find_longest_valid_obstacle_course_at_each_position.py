import bisect


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        res = []
        seq = []
        for height in obstacles:
            idx = bisect.bisect_right(seq, height)
            if idx == len(seq):
                seq.append(height)
            else:
                seq[idx] = height
            res.append(idx + 1)
        return res