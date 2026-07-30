# similar to 198. House Robber's problem, but with a circular array

# the idea is to split the problem into two subproblems:
# 1. rob the first house and not the last house
# 2. rob the last house and not the first house
# then we can use the same logic as the 198. House Robber's problem to solve the problem

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self._help(nums[1:]), self._help(nums[:-1]))

    def _help(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for i in range(len(nums)):
            new_rob = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = new_rob
        return rob2
    
