from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        firstHalf = defaultdict(int)
        secondHalf = defaultdict(int)
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                firstHalf[nums1[i] + nums2[j]] += 1
                secondHalf[nums3[i] + nums4[j]] += 1

        res: int = 0
        for n in firstHalf.keys():
            if -n in secondHalf:
                res += (firstHalf[n] * secondHalf[-n])
        return res

s = Solution()
print(s.fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))
print(s.fourSumCount(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]))