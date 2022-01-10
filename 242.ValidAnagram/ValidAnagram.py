from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ch_tabel = {}
        for ch in s:
            if (ch not in ch_tabel):
                ch_tabel[ch] = 1
            else:
                ch_tabel[ch] += 1
        for ch in t:
            if (ch not in ch_tabel):
                return False
            else:
                ch_tabel[ch] -= 1
                if (ch_tabel[ch] == 0):
                    del(ch_tabel[ch])
        if (len(ch_tabel) != 0):
            return False
        else:
            return True

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    So = Solution()
    ans = So.isAnagram(s,t)
    print(ans)