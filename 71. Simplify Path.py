class Solution:
    def simplifyPath(self, path: str) -> str:
        tmp = path.split('/')
        ans = []
        for it in tmp:
            if it == '.' or it == '':
                continue
            elif it == '..':
                if len(ans):
                    ans.pop()
            else:
                ans.append(it)
        s = '/'
        s += '/'.join(ans)
        return s

sol = Solution()
print(sol.simplifyPath('/../'))