class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        if n <= 2:
            return dp[n-1]
        for i in range (n-2):
            ans = dp[0] + dp[1]
            dp[0], dp[1] = dp[1], ans
        return dp[1]

