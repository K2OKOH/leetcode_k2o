class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = -1
        n = len(haystack)
        p = len(needle)
        if (p == 0):
            return 0
        # 初始化为-1
        next_list = [-1] * p
        self.calNext(needle, next_list)
        for idx in range(n):
            # 非首字符 & 不相等：取上一个相等的next值
            while (k>-1 and needle[k+1] != haystack[idx]):
                k = next_list[k]
            # 相等比较下一个值
            if (needle[k+1] == haystack[idx]):
                k += 1
            # 比较结束：返回首字母位置
            if (k == p-1):
                return idx - p + 1
        return -1
    
    # 计算next表
    def calNext(self, needle: str, next_list: list):
        idx_j = 1
        idx_p = -1
        # 遍历每一个字符计算next表
        while (idx_j < len(needle)):
            # 不相等&不是和第一个字符比较：上一个的next值记录
            while (idx_p > -1 and needle[idx_p+1] != needle[idx_j]):
                idx_p = next_list[idx_p]
            # 相等：看下一个字符是否相等
            if (needle[idx_p+1] == needle[idx_j]):
                idx_p += 1
            # 记录这个字符的next值
            next_list[idx_j] = idx_p
            idx_j += 1



if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    So = Solution()
    ans = So.strStr(haystack, needle)
    print(ans)