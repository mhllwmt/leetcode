class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        s = s[i:]
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        s = s[:i+1]

        s = s.split('e', maxsplit=1)
        if len(s[0]) and s[0][0] in ['-', '+']:
            s[0] = s[0][1:]
        if not self.isFloat(s[0]):
            return False
        if len(s) == 1:
            return True
        else:
            if len(s[1]) and s[1][0] in ['-', '+']:
                s[1] = s[1][1:]
            return self.isInt(s[1])

    def isFloat(self, s):  # 不考虑符号
        if len(s) == 0:
            return False
        s = s.split('.', maxsplit=1)
        if len(s) == 1:
            return self.isInt(s[0])
        elif len(s[0]) == 0 and len(s[1]) == 0:
            return False
        return self.isInt(s[0], True) and self.isInt(s[1], True)

    def isInt(self, s, flag=False): # 不考虑符号
        if len(s) == 0:
            return flag
        for it in s:
            if not '0' <= it <= '9':
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    ans = sol.isNumber("-1.e2")
    print(ans)