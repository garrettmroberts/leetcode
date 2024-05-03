from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for num in nums:
            hash_table[num] += 1

        for i in hash_table:
            if hash_table[i] == 1:
                return i
