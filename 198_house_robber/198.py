# bottom up approach
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                cache[i] = nums[i]
            elif i == 1:
                cache[i] = max(nums[i], cache[i-1])
            else:
                cache[i] = max(nums[i] + cache[i-2], cache[i-1])
    
        return cache[len(nums)-1]

# space optimized bottom up approach
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_1, rob_2 = 0, 0

        for i in range(len(nums)):
            new_rob = max(nums[i] + rob_1, rob_2)
            rob_1 = rob_2
            rob_2 = new_rob
        return rob_2

# top down approach
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(index):
            if index < 0:
                return 0
            if index in memo:
                return memo[index]
            
            memo[index] = max(nums[index] + dp(index-2), dp(index-1))
            return memo[index]
        return dp(len(nums)-1)