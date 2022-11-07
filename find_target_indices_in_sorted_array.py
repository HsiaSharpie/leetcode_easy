from typing import List


class Solution:

    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        return [idx for idx, num in enumerate(sorted_nums) if num == target]