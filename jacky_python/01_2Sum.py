from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums2idx = {}
        for i, num in enumerate(nums):
            if target - num in nums2idx.keys():
                return [nums2idx[target - num], i]
            else:
                nums2idx[num] = i


nums = [3, 2, 4]
target = 6
solution = Solution()
print (solution.twoSum(nums, target))