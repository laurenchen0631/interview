from collections import Counter
import math

def playlist(songs: list[int]):
    count = Counter(songs)
    songs.sort()
    res: int = 0

    for i in range(len(songs)-1):
        lo = max(1, math.floor((songs[i]+songs[i+1]) / 60))
        hi = (songs[i]+songs[-1]) // 60
        count[songs[i]] -= 1
        for k in range(lo, hi+1):
            target = k * 60 - songs[i]
            if target in count and count[target] > 0:
                res += count[target]
    return res

print(playlist([30,20,150,100,40]))
print(playlist([60,60,60]))
print(playlist([10, 50, 90, 30]))