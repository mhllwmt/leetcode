class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = n + m - 1
        p1, p2 = m - 1, n - 1
        while p1 >= 0 and p2 >=0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        nums1[:p2+1] = nums2[:p2+1]

if __name__ == '__main__':
    sol = Solution()
    num1 =  [1,2,3,0,0,0]
    n = 3
    num2 = [2, 5, 6]
    m = 3
    sol.merge(num1, n, num2, m)
    print(num1)


