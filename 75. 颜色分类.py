class Solution:
    def sortColors(self, nums) -> None:
        p1 = cur = 0
        p2 = len(nums) - 1
        while cur <= p2:
            if nums[cur] == 0:
                nums[cur], nums[p1] = nums[p1], nums[cur]
                p1 += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur += 1


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    sol = Solution()
    sol.sortColors(nums)
    print(nums)
