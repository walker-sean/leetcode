from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in indices:
                return [indices[comp], i]
            
            indices[num] = i