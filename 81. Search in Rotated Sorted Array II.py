class Solution:
    def search(self, nums, target) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[l] and nums[mid] == nums[r]:
                while l + 1 <= r and nums[l+1] == nums[l]:
                    l += 1
                while r - 1 >= l and nums[r-1] == nums[r]:
                    r -= 1
                if l == r:
                    return False
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

if __name__ == '__main__':
    sol = Solution()
    nums = [2, 5, 5, 5, 6, 6, 6, 6, 6, 0, 0,0,1,2]
    target = 3
    ans = sol.search(nums, target)
    print(ans)


