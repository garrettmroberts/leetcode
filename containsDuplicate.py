from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                j += 1
            else:
                return True
        return False
    
    def hasDuplicate2(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return 

solution = Solution()

print(solution.hasDuplicate([1, 2, 3, 4, 5]))  # False
print(solution.hasDuplicate([1, 1, 2, 3, 4, 5]))  # True
print(solution.hasDuplicate([1, 2, 3, 4, 5, 1]))  # True

