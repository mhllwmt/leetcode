class Solution:
    def maximalRectangle(self, matrix) -> int:
        def get_area(heights):
            n = len(heights)
            left = [0] * n
            stack = []
            zero_left = -1
            for i, num in enumerate(heights):
                if num == 0:
                    stack = []
                    zero_left = i
                    continue
                while stack and heights[stack[-1]] >= num:
                    stack.pop()
                left[i] = stack[-1] if stack else zero_left
                stack.append(i)

            right = [0] * n
            stack = []
            zero_right = n
            for i in range(n-1, -1, -1):
                num = heights[i]
                if num == 0:
                    stack = []
                    zero_right = i
                    continue
                while stack and heights[stack[-1]] >= num:
                    stack.pop()
                right[i] = stack[-1] if stack else zero_right
                stack.append(i)
            # print(left, right)
            ans = max((right[i]-left[i]-1) * heights[i] for i in range(n))
            return ans

        if not matrix:
            return 0
        n, m = len(matrix), len(matrix[0])
        heights = [0] * m
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max(ans, get_area(heights))
        return ans

if __name__ == '__main__':
    sol = Solution()
    matrix = [["1", "0", "1", "1", "1", "0"]]
    print(sol.maximalRectangle(matrix))