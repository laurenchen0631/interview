class Solution:
    # garbage = ["G","P","GP","GG"], travel = [2,4,3]
    # total collection = 6
    # total travel = (2 + 4 + 3) + (2 + 4) = 9 + 6 = 15
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        prefix = [0]
        for t in travel:
            prefix.append(prefix[-1] + t)
        last_pos = {'P': 0, 'G': 0, 'M': 0}
        total_trash = 0
        for i, units in enumerate(garbage):
            total_trash += len(units)
            for unit in units:
                last_pos[unit] = i
        
        return total_trash + prefix[last_pos['P']] + prefix[last_pos['G']] + prefix[last_pos['M']]