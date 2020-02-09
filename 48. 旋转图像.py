# class Solution:
#     def rotate(self, matrix):
#         dx = [1, 1, -1, -1]
#         dy = [1, -1, -1, 1]
#         n = len(matrix)
#
#         def my_rotate(x, y, lenth):
#             tx, ty = 0, lenth-1
#             for i in range(lenth-1):
#                 x1, y1 = x, y + i
#                 tmp = []
#                 for direct in range(4):
#                     x1 += dx[direct] * tx
#                     y1 += dy[direct] * ty
#                     tmp.append((x1, y1))
#                     tx, ty = ty, tx
#                 tx += 1
#                 ty -= 1
#                 my_swap(tmp)
#
#         def my_swap(pos):
#             f1 = matrix[pos[0][0]][pos[0][1]]
#             for i in range(1, 4):
#                 matrix[pos[i][0]][pos[i][1]], f1 = f1, matrix[pos[i][0]][pos[i][1]]
#             matrix[pos[0][0]][pos[0][1]] = f1
#
#         x = y = 0
#         for num in range(n, 1, -2):
#             my_rotate(x, y, num)
#             x += 1
#             y += 1



class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                print(i, j)
                tmp = [0] * 4
                row, col = i, j
                # store 4 elements in tmp
                for k in range(4):
                    tmp[k] = matrix[row][col]
                    row, col = col, n - 1 - row
                # rotate 4 elements
                for k in range(4):
                    matrix[row][col] = tmp[(k - 1) % 4]
                    row, col = col, n - 1 - row

sol = Solution()
matrix = [[1,2,3,4,5], [10, 4, 5, 6, 5], [11, 7, 8, 9, 5], [-1, -2, -3, -4, 5], [1,2,3,4,5]]
sol.rotate(matrix)
print(matrix)