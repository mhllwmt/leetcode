class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for it in digits:
            num = num * 10 + it
        num += 1
        ans = [ int(it) for it in "".join(str(num)) ]
        print(ans)
        return ans

if __name__ == '__main__':
    sol = Solution()
    sol.plusOne([1, 2, 3])
