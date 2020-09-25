from collections import Counter
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def is_equal(s1, s2):
            s1 = Counter(s1)
            s2 = Counter(s2)
            return s1 == s2

        def isok(s1, s2, l1, r1, l2, r2):
            if l1 == r1:
                return s1[l1] == s2[l2]
            for i in range(l1, r1):
                num = i - l1 + 1
                tmp_s1 = s1[l1: l1+num]
                tmp_s2 = s2[l2: l2+num]
                if is_equal(tmp_s1, tmp_s2):
                    # print(l1, r1, l2, r2, tmp_s1, tmp_s2)
                    mid1, mid2 = l1 + num - 1, l2 + num - 1
                    if isok(s1, s2, l1, mid1, l2, mid2) and isok(s1, s2, mid1 + 1, r1, mid2 + 1, r2):
                        return True
                tmp_s2 = s2[r2-num+1:r2+1]
                # print(l1, r1, l2, r2, tmp_s1, tmp_s2)
                if is_equal(tmp_s1, tmp_s2):
                    mid1, mid2 = l1 + num - 1, r2 - num
                    if isok(s1, s2, l1, mid1, mid2 + 1, r2) and isok(s1, s2, mid1 + 1, r1, l2, mid2):
                        return True
            return False
        n = len(s1)
        return False if not is_equal(s1, s2) else isok(s1, s2, 0, n - 1, 0, n - 1)

if __name__ == '__main__':
    s1 = "great"
    s2 = "rgeat"
    sol = Solution()
    ans = sol.isScramble(s1, s2)
    print(ans)