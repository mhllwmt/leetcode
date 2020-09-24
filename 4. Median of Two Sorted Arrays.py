class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n, m = len(nums1), len(nums2)
        left = (n + m + 1) // 2
        right = (n + m + 2) // 2
        def get_kth(nums1, nums2, k):
            if len(nums1) > len(nums2):
                nums1, nums2 = nums2, nums1
            n, m = len(nums1), len(nums2)
            l1 = l2 = 0
            r1, r2 = n-1, m-1
            while k != 1 and l1 <= r1 and l2 <= r2:
                t1,  t2 = min(r1, l1 + k // 2 - 1), l2 + k // 2 - 1
                if nums1[t1] <= nums2[t2]:  # 小于号好重要
                    k -= t1 - l1 + 1
                    l1 = t1 + 1
                else:
                    k -= t2 - l2 + 1
                    l2 = t2 + 1
                # print(l1, l2, k)
            # print("#"*16)
            if l1 > r1: return nums2[l2 + k -1]
            elif l2 > r2: return nums1[l1 + k - 1]
            else:         return  min(nums1[l1], nums2[l2])

        return (get_kth(nums1, nums2, left) + get_kth(nums1, nums2, right)) * 0.5

if __name__ == '__main__':
    sol = Solution()
    nums1 = [0, 0, 0]
    nums2 = [1, 1, 1]
    print(sol.findMedianSortedArrays(nums1, nums2))
