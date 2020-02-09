import copy

class Solution:
    def solveNQueens(self, n: int):
        dt = []
        ans = []

        def queen(A, cur=0):
            if cur == n:
                dt.append(copy.copy(A))
                return

            for col in range(n):
                flag = True
                for row in range(cur):
                    if A[row] == col or abs(A[row] - col) == cur - row:
                        flag = False
                        break
                if flag:
                    A[cur] = col
                    queen(A, cur + 1)

        A = [None] * n
        queen(A)
        for it in dt:
            tmp = [['.'] * n for _ in range(n)]
            for row in range(n):
                tmp[row][it[row]] = 'Q'
                tmp[row] = ''.join(tmp[row])
            ans.append(tmp)
        return ans

sol = Solution()
print(sol.solveNQueens(4))