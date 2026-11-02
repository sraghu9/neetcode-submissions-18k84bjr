class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = [[None] * 2 for _ in range(len(nums))]

        def dfs(i, flag):
            if i == len(nums) - 1:
                return max(0, nums[i]) if flag else nums[i]
            if memo[i][flag] is not None:
                return memo[i][flag]
            if flag:
                memo[i][flag] = max(0, nums[i] + dfs(i + 1, True))
            else:
                memo[i][flag] = max(dfs(i + 1, False),
                                    nums[i] + dfs(i + 1, True))
            return memo[i][flag]

        return dfs(0, False)