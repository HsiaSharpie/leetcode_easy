from typing import List


class Solution:

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        map_dict = {num: idx + 1 for idx, num in enumerate(sorted_arr)}
        return [map_dict[x] for x in arr]