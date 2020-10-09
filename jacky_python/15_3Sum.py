from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_len = len(nums)
        res = []
        
        for i in range(nums_len-2):
            if i != 0:
                if nums[i] == nums[i-1]: continue
            
            j = i + 1
            k = nums_len - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                
                if three_sum == 0: 
                    res.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    
                    j += 1
                    k -= 1 

                elif three_sum < 0: 
                    j += 1
                elif three_sum > 0: 
                    k -= 1

        return res
                


nums = [-1,0,1,2,-1,-4]
solution = Solution()
print (solution.threeSum(nums))