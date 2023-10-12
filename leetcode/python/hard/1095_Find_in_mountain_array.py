# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def __init__(self) -> None:
        self.cache = dict[int,int]()
        self.arr: 'MountainArray' = None
        
    def get(self, k: int) -> int:
        if k not in self.cache:
            self.cache[k] = self.arr.get(k)
        return self.cache[k]
    
    def find_peak(self) -> int:
        l, r = 1, self.arr.length() - 2
        while l < r:
            m = (l + r) // 2
            if self.get(m) < self.get(m + 1):
                l = m + 1
            else:
                r = m
        return l
    
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        self.arr = mountain_arr
        peak = self.find_peak()
        
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            if self.get(m) == target:
                return m
            elif self.get(m) < target:
                l = m + 1
            else:
                r = m - 1
                
        l, r = peak, self.arr.length() - 1
        while l <= r:
            m = (l + r) // 2
            if self.get(m) == target:
                return m
            elif self.get(m) < target:
                r = m - 1
            else:
                l = m + 1
        
        return -1
        