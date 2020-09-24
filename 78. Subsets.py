class Solution:
    def subsets(self, num):
        ans = []
        tmp = []
        def get_subset(index, tmp):
            if index == len(num):
                t = tmp[:]
                ans.append(t)
                return

            get_subset(index+1, tmp)
            tmp.append(num[index])
            get_subset(index+1, tmp)
            tmp.pop()
        get_subset(0, tmp)
        return ans

if __name__ == '__main__':
    x = [1, 2, 3]
    sol = Solution()
    ans = sol.subsets(x)
    print(ans)

