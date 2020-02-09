from collections import Counter
import copy

class Solution:
    def permuteUnique(self, nums):
        nums = Counter(nums).most_common()
        ans = [[nums[0][0]] * nums[0][1]]

        def add_items(insert_index, key, per):
            for item in per:
                tmp , start = [], 0
                for end in insert_index:
                    tmp += item[start: end] + [key]
                    start = end
                tmp += item[start: ]
                ans.append(tmp)

        for i in range(1, len(nums)):
            key, num = nums[i]
            coms = self.combination(len(ans[0]), num)
            tmp, ans = ans, []
            for item in coms:
                add_items(item, key, tmp)
        # print(len(ans))
        return  ans

    @staticmethod
    def combination(n, m):
        ans = []

        def dfs(start, num, tmp):
            if num == 0:
                ans.append(tmp)
                return
            for i in range(start, n+1):
                tm = copy.copy(tmp)
                tm.append(i)
                dfs(i, num-1, tm)

        dfs(0, m, [])
        # print(len(ans))
        return ans


sol = Solution()
ans = sol.permuteUnique([1, 1, 1, 2, 2, 3, 3])
print(ans)