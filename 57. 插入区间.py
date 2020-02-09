# class Solution:
#     def insert(self, intervals, newInterval):
#         def union(x, y):
#             if y[0] < x[0]:
#                 x, y = y, x
#             if  x[1] >= y[0]:
#                 return [x[0], max(x[1], y[1])]
#             else:
#                 return None
#
#         i, n = 0, len(intervals)
#         ans = []
#         while i < n and union(intervals[i], newInterval) is None:
#             if newInterval[1] < intervals[i][0]:
#                 break
#             ans.append(intervals[i])
#             i += 1
#         while i < n:
#             tmp = union(intervals[i], newInterval)
#             if tmp is None:
#                 break
#             else:
#                 newInterval = tmp
#             i += 1
#         ans.append(newInterval)
#         ans += intervals[i:]
#         return ans

# 法二
class Solution:
    def insert(self, intervals, newInterval):
        # 1 首先找到插入位置，位于其之前的所有区间输出到output
        # 2 对于之前的所有区间 判定最后新区间是否需要与之前的最后一个区间合并， 还是直接放入；
        # 3 合并之后的区间
        i, n = 0, len(intervals)
        ans = []

        while i < n and intervals[i][0]  <  newInterval[0]:
            ans.append(intervals[i])
            i += 1

        if not ans or ans[-1][1] < newInterval[0]:
            ans.append(newInterval)
        else:
            ans[-1][1] = max(ans[-1][1], newInterval[1])

        while i < n:
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])
            i += 1

        return ans

sol = Solution()
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(sol.insert(intervals, newInterval))
