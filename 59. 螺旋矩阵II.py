class Solution:
    def generateMatrix(self, n: int):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        ans = [[None] * n for _ in range(n)]

        def isok(x, y):
            return  0 <= x < n and 0 <= y < n and ans[x][y] is None

        i = x = y = flag = 0
        while i < n*n:
            ans[x][y] = i + 1
            if i + 1 == n*n:
                break
            while True:
                tx = x + dx[flag]
                ty = y + dy[flag]
                if isok(tx, ty):
                    x, y = tx, ty
                    break
                else:
                    flag = (flag + 1) % 4
            i += 1
        return ans

sol = Solution()
print(sol.generateMatrix(3))
