from typing import List

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cnt = 0
        pre = 0
        cur = 1
        for idx in range(1,len(s)):
            if (s[idx-1] == s[idx]):
                cur += 1
            else:
                pre = cur
                cur = 1
            if (pre>=cur):
                cnt += 1
        return cnt


if __name__ == '__main__':
    s = "00110011"
    So = Solution()
    ans = So.countBinarySubstrings(s)
    print(ans)