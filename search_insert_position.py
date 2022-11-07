from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = len(nums) - 1
        last_value = nums[idx]

        while last_value >= target:
            idx -= 1
            last_value = nums[idx]

            if idx < 0:
                return 0
        return idx + 1