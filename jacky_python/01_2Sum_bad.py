from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """ 
            Create invert idx map.
        """
        num_idx_map = {}
        for idx, num in enumerate(nums):
            num_idx_map[num] = num_idx_map.get(num, [])
            num_idx_map[num].append(idx)
        
        nums.sort()
        
        
        """ 
           Method like 15_3Sum
        """
        i = 0
        j = len(nums) - 1
        while i < j:
            two_sum = nums[i] + nums[j]

            if two_sum == target: 
                if nums[i] == nums[j]:
                    return num_idx_map[nums[i]]
                else:
                    return [ num_idx_map[nums[i]][0], num_idx_map[nums[j]][0] ]
            
            elif two_sum < target:
                i += 1
                while nums[i] == nums[i-1]:
                    i += 1

            elif two_sum > target:
                j -= 1
                while nums[j] == nums[j+1]:
                    j -= 1


nums = [3, 2, 4]
target = 6
solution = Solution()
print (solution.twoSum(nums, target))