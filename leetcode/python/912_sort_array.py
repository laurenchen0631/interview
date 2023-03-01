class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def heapify(i: int, n: int) -> None:
            l, r = 2 * i + 1, 2 * i + 2
            largest = i
            if l < n and nums[l] > nums[largest]:
                largest = l
            if r < n and nums[r] > nums[largest]:
                largest = r
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(largest, n)
        
        def heapsort() -> None:
            for i in range(len(nums) // 2 - 1, -1, -1):
                heapify(i, len(nums))
            # move the largest element to the end and heapify the rest
            for i in range(len(nums) - 1, 0, -1):
                nums[0], nums[i] = nums[i], nums[0]
                heapify(0, i)
        
        heapsort()
        return nums
        
s = Solution()
print(s.sortArray([5,2,3,1]))
print(s.sortArray([5,1,1,2,0,0]))