import copy


class Solution:
    def permute(self, nums):
        n = len(nums)
        vis = [False] * n
        ans = []

        def dfs(idx, tmp):
            tmp.append(nums[idx])
            if len(tmp) == n:
                ans.append(tmp)
                return
            vis[idx] = True
            for i in range(n):
                if not vis[i]:
                    dfs(i, copy.copy(tmp))
            vis[idx] = False

        for i in range(n):
            dfs(i, [])
        return ans


sol = Solution()
ans = sol.permute([1, 2, 3, 4])
print(ans)