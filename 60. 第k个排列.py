class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        base,  ans = 1, []
        nums = [str(i) for i in range(1, n+1)]
        for i in range(1, n):
            base *= i
        for i in range(n-1, 0, -1):
            inx = k // base
            k -= base * inx
            base //= i
            ans.append(nums[inx])
            nums = nums[:inx] + nums[inx+1:]
        ans.append(nums[0])
        return ''.join(ans)

sol = Solution()
print(sol.getPermutation(3, 3))