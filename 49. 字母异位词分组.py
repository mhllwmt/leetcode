class Solution:
    def groupAnagrams(self, strs):
        ans = []
        dc = dict()
        for it in strs:
            s = ''.join(sorted(it))
            if s not in dc:
                dc[s] = len(ans)
                ans.append([it])
            else:
                ans[dc[s]].append(it)
        return ans

cin = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
print(sol.groupAnagrams(cin))