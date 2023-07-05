class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ouput = []
        for i  in range(len(nums)):
            num2 = target-nums[i]
            for j in range(i+1,len(nums)):
                if num2 == nums[j]:
                    ouput.append(i)
                    ouput.append(j)
                    return ouput 
                    break


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        filtered_nums = {}
        for i,num in enumerate(nums):
            num2 = target-num
            if num2 in filtered_nums:
                return [filtered_nums[num2],i]
            else:
                filtered_nums[num] = i
        return                           