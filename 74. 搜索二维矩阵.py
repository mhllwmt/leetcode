class Solution:
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        l, h = 0, n * m - 1
        while l <= h:
            mid = (l + h) // 2
            x = matrix[mid // m][mid % m]
            # print(mid, x, target)
            if x == target:
                return True
            elif x < target:
                l = mid + 1
            else:
                h = mid - 1
        return False


if __name__ == '__main__':
    sol = Solution()
    matrix = eval(input())
    target = eval(input())
    print(target, matrix)
    print(sol.searchMatrix(matrix, target))
