class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        pass

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        pass

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        pass

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        pass

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        pass

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        pass

class Solution:
    def depthSumInverse(self, nestedList: list[NestedInteger]) -> int:
        maxDepth, sum, weightedSum = self._helper(nestedList, 1)
        return (maxDepth+1)*sum - weightedSum

    def _helper(self, nested: list[NestedInteger], depth: int) -> tuple[int, int, int]:
        sum: int = 0
        weightedSum: int = 0
        maxDepth = depth

        print(type(nested))
        for item in nested:
            if item.isInteger():
                sum += item.getInteger()
                weightedSum += item.getInteger() * depth
            else:
                res = self._helper(item.getList(), depth+1)
                sum += res[1]
                weightedSum += res[2]
                maxDepth = max(maxDepth, res[0])
          
        return (maxDepth, sum, weightedSum)