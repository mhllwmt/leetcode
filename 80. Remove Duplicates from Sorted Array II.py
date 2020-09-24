class Solution:
    def removeDuplicates(self, nums) -> int:
        cnt = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[cnt] or  cnt == 0 or nums[i] != nums[cnt-1]:
                cnt += 1
                nums[cnt] = nums[i]
        print(nums[:cnt+1])
        return cnt+1


if __name__ == '__main__':
    sol = Solution()
    ans = sol.removeDuplicates([0,0,1,1,1,1,2,3,3])
    print(ans)