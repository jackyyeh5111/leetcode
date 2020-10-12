from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        res = sum(nums[:3])
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if abs(three_sum - target) < abs(res - target):
                    res = three_sum
                
                if three_sum == target: 
                    return target
                
                elif three_sum < target:
                    while j < k and nums[j+1] == nums[j]:
                        j += 1    
                    j += 1

                elif three_sum > target:
                    while j < k and nums[k-1] == nums[k]:
                        k -= 1    
                    k -= 1
        
        return res


nums = [-1,2,1,-4]
target = 1
solution = Solution()
print (solution.threeSumClosest(nums, target))