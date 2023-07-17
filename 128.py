"""
Not using set.
Time Limit Exceeded in case 68


"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        long = []
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        for n in nums:
            if n-1 not in nums:
                x=1
                while n+x in nums:
                    x+=1
                if x > 1:
                    long.append(x)
                elif x == 1:
                    long.append(1)
            else:
                continue
        if len(long) >=1:            
            while len(long) > 1:
                for i in range(len(long)):
                    if i+1 < len(long):
                        if long[i] <= long[i+1]: 
                            long.pop(i)
                        else:
                            long.pop(i+1)
                    else:
                        break
            return long[0]            
        else:
            return 0  



"""
Use set to clear number in nums.
If nums-1 is not in seted nums, nums was the first number of sequence
"""      
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long = []
        seted_nums = set(nums)
        for n in seted_nums:
            if n-1 not in seted_nums:
                x=1
                while n+x in seted_nums:
                    x+=1
                if x > 1:
                    long.append(x)
                elif x == 1:
                    long.append(1)
                else:
                    continue    
        if len(long) >=1:            
            while len(long) > 1:
                for i in range(len(long)):
                    if i+1 < len(long):
                        if long[i] <= long[i+1]: 
                            long.pop(i)
                        else:
                            long.pop(i+1)
                    else:
                        break
            return long[0]            
        else:
            return 0                
                        
        