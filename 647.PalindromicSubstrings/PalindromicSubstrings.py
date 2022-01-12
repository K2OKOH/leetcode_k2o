from typing import List

class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for idx in range(len(s)):
            cnt += self.count_ch(s, idx, idx)
            cnt += self.count_ch(s, idx, idx+1)
        return cnt
    
    def count_ch(self, s: str, l: int, r: int):
        cnt_ch = 0
        while(l>=0 and r<len(s) and s[l]==s[r]):
            l -= 1
            r += 1
            cnt_ch += 1
        return cnt_ch


if __name__ == '__main__':
    s = "aaa"
    So = Solution()
    ans = So.countSubstrings(s)
    print(ans)