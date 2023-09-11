class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        groups = {}
        for id, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = [[]]
            elif len(groups[size][-1]) == size:
                groups[size].append([])
            
            groups[size][-1].append(id)
        
        res = []
        for subgroups in groups.values():
            res.extend(subgroups)
        return res
        
        