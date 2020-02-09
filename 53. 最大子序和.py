class Solution:
    def maxSubArray(self, nums):
        num_max = max(nums)
        if num_max <= 0:
            return num_max

        ans = tmp = 0
        for num in nums:
            tmp += num
            if tmp < 0:
                tmp = 0
            else:
                ans = max(ans, tmp)
        return ans

sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,-1]
print(sol.maxSubArray(nums))