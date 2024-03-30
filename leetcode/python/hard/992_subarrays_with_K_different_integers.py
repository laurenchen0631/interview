from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        return self.slidingWindowAtMost(nums, k) - self.slidingWindowAtMost(nums, k - 1)

    # Helper function to count the number of subarrays with at most k distinct elements.
    def slidingWindowAtMost(self, nums: list[int], k: int) -> int:
        # To store the occurrences of each element.
        freq_map = defaultdict(int)
        left = 0
        total_count  = 0

        # Right pointer of the sliding window iterates through the array.
        for right, vr in enumerate(nums):
            freq_map[vr] += 1

            # If the number of distinct elements in the window exceeds k,
            # we shrink the window from the left until we have at most k distinct elements.
            while len(freq_map) > k:
                freq_map[nums[left]] -= 1
                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]
                left += 1

            # Update the total count by adding the length of the current subarray.
            total_count  += right - left + 1

        return total_count 