class Solution:
    def totalNQueens(self, n):
        global ans
        ans = 0

        def queen(A, cur=0):
            global ans
            if cur == n:
                ans += 1
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

        A = [None] * 8
        queen(A)
        return ans

sol = Solution()
print(sol.totalNQueens(4))