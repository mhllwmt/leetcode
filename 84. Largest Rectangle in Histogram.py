class Solution:
    def largestRectangleArea(self, heights):
        def get_max(heights):
            stack = []
            ans = [0] * len(heights)
            nums = heights + [0]
            for i, num in enumerate(nums):
                if len(stack) == 0 or nums[stack[-1]] <= num:
                    stack.append(i)
                elif nums[stack[-1]] > num:
                    while len(stack)!=0 and nums[stack[-1]] > num:
                        ans[stack[-1]] = i - 1
                        stack.pop()
                    stack.append(i)
            return ans

        r_heights = get_max(heights)
        l_heights = get_max(heights[::-1])[::-1]
        ans, n = 0, len(heights)
        for i in range(n):
            ans = max(ans, heights[i] * (r_heights[i] - (n - 1 - l_heights[i]) + 1))
        return ans


if __name__ == '__main__':
    sol = Solution()
    heights = [2,1,5,1,4,100,3,3]
    ans = sol.largestRectangleArea(heights)
    print(ans)

