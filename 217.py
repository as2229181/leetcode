
"""
First method 


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:    
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                duplicate = True
                break
            else:
                 duplicate= False    
         return duplicate
 
 Outcome not pass  Time Limit Exceeded 65 / 74 testcases passed
 """
"""
second try pass

class Solution:
    def containsDuplicate(self, nums) -> bool:
        sort_num=sorted(nums)    
        for i in range(1,len(sort_num)):
            if sort_num[i] == sort_num[i-1]:
                        duplicate = True
                        break

        return duplicate

        Runtime 611 ms
        Memory 28.4 MB

"""

"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:    
        filter_num=set()
        duplicate = False
        for n in nums:
            if n in filter_num :
                duplicate = True
                break
            else:
                filter_num.add(n)    
        return duplicate

Runtime
548 ms
Memory
30.9 MB

"""

