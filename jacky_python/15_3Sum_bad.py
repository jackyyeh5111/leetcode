from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_len = len(nums)
        res = []
        for i in range(nums_len-2):
            for j in range(i+1, nums_len-1):
                for k in range(j+1, nums_len):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
        
        """ 
            Python cannot use list(set(obj)) to get unique list of obj
            if the type of obj is list of lists.

            Alternative is to use dict to store the unique key.
        """
        unique_res = {}
        for item in res:
            unique_res[tuple(item)] = None # None is randomly assigned
        
        res = [list(key) for key in unique_res.keys()]
        return res

nums = [-1,0,1,2,-1,-4]
solution = Solution()
print (solution.threeSum(nums))