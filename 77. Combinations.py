import copy

class Solution:
    def combine(self, n: int, k: int):
        ans = []

        def generate(id, tmp):
            if len(tmp) == k:
                ans.append(tmp[:]) # 有效复制
                return
            if n - id + 1 + len(tmp) < k:
                return
            for i in range(id, n+1):
                tmp.append(i)
                generate(i+1, tmp)
                tmp.pop()

        generate(1, [])
        return ans
if __name__ == '__main__':
    sol = Solution()
    ans = sol.combine(5, 3)
    print(ans)

