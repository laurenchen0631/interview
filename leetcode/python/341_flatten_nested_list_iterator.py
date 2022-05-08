from this import d


class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """
       pass

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """
       pass

   def getList(self) -> list[NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """
       pass


class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        self.stack = [[nestedList, 0]]
    
    def next(self) -> int:
        self._dfs()
        i = self.stack[-1][1]
        self.stack[-1][1] += 1
        return self.stack[-1][0][i].getInteger()
        
    def hasNext(self) -> bool:
        self._dfs()
        return len(self.stack) > 0

    def _dfs(self) -> None:
        while self.stack:
            cur = self.stack[-1][0]
            i = self.stack[-1][1]
            if len(cur) <= i:
                self.stack.pop()
                continue
            if cur[i].isInteger():
                break
            self.stack[-1][1] += 1
            self.stack.append([cur[i].getList(), 0])
         
