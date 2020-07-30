class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        ans = []
        i = 0
        k = 0
        while i < len(a) or i < len(b):
            x = y = 0
            if i < len(a):
                x = int(a[i])
            if i < len(b):
                y = int(b[i])
            num = x + y + k
            ans.append(str(num%2))
            k = num // 2
            i += 1
        if k != 0:
            ans.append(str(k))
        ans = ans[::-1]
        return ''.join(ans)


sol  = Solution()
ans = sol.addBinary("1010", "1011")
print(ans)