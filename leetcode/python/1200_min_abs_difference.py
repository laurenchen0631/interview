class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        sortedArr = sorted(arr)
        if len(sortedArr) < 2:
            return []
        print(sortedArr)

        minVal: int = abs(sortedArr[0] - sortedArr[1])
        res: list[list[int]] = []
        for i in range(len(sortedArr) - 1):
            diff = abs(sortedArr[i] - sortedArr[i+1])
            if diff < minVal:
                minVal = diff
                res.clear()
            if diff == minVal:
                res.append([sortedArr[i], sortedArr[i+1]])


        return res
        
if __name__ == '__main__':
  s = Solution()
  print(s.minimumAbsDifference([1]))
  print(s.minimumAbsDifference([1,9]))
  print(s.minimumAbsDifference([4,2,1,3]))
  print(s.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))
  print(s.minimumAbsDifference([40,11,26,27,-20]))