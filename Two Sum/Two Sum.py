from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,j in enumerate(nums):
            c = target - j 
            if c in seen:
                return [seen[c],i]
            seen[j] = i