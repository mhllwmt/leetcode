class Solution:
    def grayCode(self, k: int):
        def binary2int(s: str) ->int:
            ans = 0
            for item in s:
                k = 1 if item == '1' else 0
                ans = ans * 2 + k
            return ans

        ans = ['0'*k]
        base = 1
        for i in range(k):
            for j in range(base):
                tmp = list(ans[base - j - 1])
                tmp[-i-1] = '1'
                ans.append(''.join(tmp))
            base *= 2
        ans = [binary2int(it) for it in ans]
        return ans

# 优秀代码
# class Solution:
#     def grayCode(self, n: int) -> List[int]:
#         res, head = [0], 1
#         for i in range(n):
#             for j in range(len(res) - 1, -1, -1):
#                 res.append(head + res[j])
#             head <<= 1
#         return res



if __name__ == '__main__':
    sol = Solution()
    ans =  sol.grayCode(2)
    print(ans)