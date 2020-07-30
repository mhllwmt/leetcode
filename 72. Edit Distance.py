class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [ [0]*(l2+1) for _ in range(l1+1) ]
        for i in range(l1+1):
            dp[i][0] = i
        for j in range(l2+1):
            dp[0][j] = j
        for i in range(l1):
            for j in range(l2):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1 # insert delete replace
        return dp[l1][l2]





sol = Solution()
s1 = "intention"
s2 = "execution"
ans = sol.minDistance(s1, s2)
print(ans)