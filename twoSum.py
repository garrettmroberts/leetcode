from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        
    
solution = Solution()

print(solution.twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(solution.twoSum([-1,-2,-3,-4,-5], -8))  # [2, 4]