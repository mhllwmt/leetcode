class Solution:
    def spiralOrder(self, matrix):
        if not len(matrix):
            return matrix

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = direct = 0
        n, m = len(matrix), len(matrix[0])
        ans = []

        def isok(x, y):
            if 0 <= x < n and 0 <= y < m and matrix[x][y] is not None:
                return True
            return False
        for _ in range(n*m):
            ans.append(matrix[x][y])
            matrix[x][y] = None
            if _ == n*m - 1:
                break
            while True:
                tx = x + dx[direct]
                ty = y + dy[direct]
                if isok(tx, ty):
                    x, y = tx, ty
                    break
                else:
                    direct = (direct + 1) % 4
        return ans

sol = Solution()
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(sol.spiralOrder(matrix))
