class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x
        while l < h:
            a = (l + h + 1) // 2
            b = x // a
            if b >= a:
                l = a
            else:
                h = a - 1
        return l

sol = Solution()
print(sol.mySqrt(170))