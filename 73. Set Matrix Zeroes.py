class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        s1 = set()
        s2 = set()
        l1 = len(matrix)
        l2 = 0 if l1==0 else len(matrix[0])
        for i in range(l1):
            for j in range(l2):
                if matrix[i][j] == 0:
                    s1.add(i)
                    s2.add(j)
        for i in range(l1):
            for j in range(l2):
                if i in s1 or j in s2:
                    matrix[i][j] = 0