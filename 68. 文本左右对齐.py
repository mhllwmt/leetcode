class Solution:
    def fullJustify(self, words, maxWidth):
        i = 0
        ans = []
        while i < len(words):
            tmp = []
            num = sum_len = 0
            while i < len(words) and (num + sum_len + len(words[i])) <= maxWidth:
                tmp.append(words[i])
                sum_len += len(words[i])
                num += 1
                i += 1

            if i == len(words):
                blank = [1] * (num - 1) + [maxWidth - sum_len - num + 1]
            elif num == 1:
                blank = [maxWidth - sum_len]
            else:
                blank = [(maxWidth - sum_len) // (num - 1)] * (num - 1)
                for k in range ((maxWidth - sum_len) % (num - 1)):
                    blank[k] += 1
                blank += [0]
            string = ""
            for k, s in enumerate(tmp):
                string += s + " " * blank[k]
            # print(string + "#")
            ans.append(string)
        return ans


sol = Solution()
s = input()
s = eval(s)
sol.fullJustify(s, 20)
