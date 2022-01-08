class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        elements: dict[int,int] = {}
        for n in nums:
            elements[n] = elements.get(n, 0) + 1
        res: list[list[int]] = []
        self.helper(elements, [], res, len(nums))
        return res
    
    def helper(self, elements: dict[int,int], perm: list[int], res: list[list[int]], n: int) -> None:
        if len(perm) == n:
            return res.append(perm.copy())

        for k in elements.keys():
            if elements[k] == 0:
                continue
            perm.append(k)
            elements[k] -= 1
            self.helper(elements, perm, res, n)
            elements[k] += 1
            perm.pop()

if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1,1,2]))
    print(s.permuteUnique([1,2,3]))