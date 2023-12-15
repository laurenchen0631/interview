class Solution:
    #  [["B","C"],["D","B"],["C","A"]]
    def destCity(self, paths: list[list[str]]) -> str:
        dest = set[str]()
        points = set[str]()
        
        for u, v in paths:
            points.add(u)
            if u in dest:
                dest.remove(u)
            if v not in points:
                dest.add(v)
        return dest.pop()
            
        