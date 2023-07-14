"""
time complexity n*k
space complexity n
 """

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        output = [[] for i in range(len(nums)+1)]
        for n in nums:
            dic[n] = 1+dic.get(n,0)
        for key,value in dic.items():
            output[value].append(key)
        res = []
        c=0
        for i in range(len(nums),0,-1):            
            if len(output[i]) > 0 and len(res)<k:
                for j in output[i]:
                    res.append(j)
                c+=1
        
        return res