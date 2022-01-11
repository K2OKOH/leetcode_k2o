from typing import List

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        in_list = ([-1]*256)
        out_list = ([-1]*256)
        len_w = len(s)
        for idx in range(len_w):
            in_idx = ord(s[idx])
            out_idx = ord(t[idx])
            # 没有见过这个字母映射
            if (in_list[in_idx] == -1 and out_list[out_idx] == -1):
                # 写入目标字母
                in_list[in_idx] = out_idx
                out_list[out_idx] = in_idx
            # 已经存在映射
            elif (in_list[in_idx] != -1 or out_list[out_idx] != -1):
                if (in_list[in_idx] != out_idx or out_list[out_idx] != in_idx):
                    return False
        return True

if __name__ == '__main__':
    s = "badc"
    t = "baba"
    So = Solution()
    ans = So.isIsomorphic(s,t)
    print(ans)