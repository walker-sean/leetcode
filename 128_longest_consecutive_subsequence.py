from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        
        for num in nums:
            count = 1
            curr = num
            while curr + 1 in nums:
                count += 1
                curr += 1
            longest = max(max, count)
        return longest
                