class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda it : (it[0],it[1]))
        ans = []
        prex = None
        for it in intervals:
            if prex is None:
                prex = it
            elif prex[0] <= it[0] <= prex[1]:
                prex[1] = max(it[1], prex[1])
            else:
                ans.append(prex)
                prex = it
        if prex is not None:
            ans.append(prex)
        return ans

sol = Solution()
intervals = [[1,4], [4, 8]]
print(sol.merge(intervals))
