nums = [1,2,3,4]
pre = []
suf = []
ouput = [0] * len(nums)


for i in range(len(nums)):
    if i == 0 :
        pre.append(1)
        suf_num =1
        for numb in nums[i+1:]:
            suf_num = suf_num*numb
        suf.append(suf_num)    
    elif i == len(nums)-1:
        suf.append(1)
        pre_num = 1
        for numa in nums[:i]:
            pre_num = pre_num*numa
        pre.append(pre_num)
    else:
        suf_num =1
        pre_num = 1
        for numb in nums[i+1:]:
            suf_num = suf_num*numb
        for numa in nums[:i]:
            pre_num = pre_num*numa
        pre.append(pre_num)
        suf.append(suf_num)
    ouput[i] = pre[i]*suf[i]
print (pre)
print (suf)
print (ouput)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        suf = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] = pre
            pre = pre*nums[i]
        for j in range(len(nums)-1,-1,-1):
            output[j] = output[j]*suf
            suf *= nums[j] 
        return output         


"""
Not pass cause there second layer for loop
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        suf = []
        ouput = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0 :
                pre.append(1)
                suf_num =1
                for numb in nums[i+1:]:
                    suf_num = suf_num*numb
                suf.append(suf_num)    
            elif i == len(nums)-1:
                suf.append(1)
                pre_num = 1
                for numa in nums[:i]:
                    pre_num = pre_num*numa
                pre.append(pre_num)
            else:
                pre_num = 1
                suf_num =1
                for numb in nums[i+1:]:
                    suf_num = suf_num*numb
                for numa in nums[:i]:
                    pre_num = pre_num*numa
                pre.append(pre_num)
                suf.append(suf_num)
            ouput[i] = pre[i]*suf[i]
        return ouput   