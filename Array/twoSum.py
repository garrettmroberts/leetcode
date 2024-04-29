from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            needed_num = target - nums[i]
            if needed_num in d:
                return [d[needed_num], i]
            d[nums[i]] = i

        return [0, 1]
