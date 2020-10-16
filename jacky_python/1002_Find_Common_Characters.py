from typing import List

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        res = dict()
        for i, str_ in enumerate(A):
            
            if i == 0:
                for char in str_:
                    res[char] = res.get(char, 0) + 1
            else:
                sub_res = dict()
                for char in str_:
                    if char in res.keys() and sub_res.get(char, 0) + 1 <= res[char]:
                        sub_res[char] = sub_res.get(char, 0) + 1
                
                res = sub_res

        final_res = []
        for key, value in res.items():
            final_res = final_res + [key] * value
        
        return final_res


A = ["bella","label","roller"]
solution = Solution()
print (solution.commonChars(A))