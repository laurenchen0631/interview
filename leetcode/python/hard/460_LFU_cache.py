from collections import OrderedDict, defaultdict
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict[int, tuple[int, int]]()
        self.freq = defaultdict(OrderedDict[int, bool])
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        return self._update(key, self.cache[key][1])
    
    def _update(self, key: int, value: int) -> int:
        f, _ = self.cache[key]
        self.freq[f].pop(key)
        if f == self.minFreq and not self.freq[f]:
            self.minFreq = f+1
        
        f += 1
        self.cache[key] = (f, value)
        self.freq[f][key] = True
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            self._update(key, value)
        else:
            if len(self.cache) == self.capacity:
                least, _ = self.freq[self.minFreq].popitem(last=False)
                self.cache.pop(least)
            self.cache[key] = (1, value)
            self.minFreq = 1
            self.freq[1][key] = True
