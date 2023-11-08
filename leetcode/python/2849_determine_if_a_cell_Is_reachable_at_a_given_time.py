class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            return t != 1
            
        d = (1 if fx > sx else -1, 1 if fy > sy else -1)
        min_time_required = min(abs(fx-sx), abs(fy-sy))
        [sx, sy] = [sx + min_time_required * d[0], sy + min_time_required * d[1]]
        min_time_required += abs(fx-sx) + abs(fy-sy)
        return min_time_required <= t
        
        