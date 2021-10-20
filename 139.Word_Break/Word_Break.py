from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        num_s = len(s)
        # 共有num_s+1个可以分割的点，包括首尾
        dp = [False] * (num_s+1)
        dp[0] = True
        for idx in range(num_s+1):
            for word in wordDict:
                # 对每个位置，看每个单词是否能分割
                length = len(word)
                a = s[idx-length:idx]
                if(idx>=length and s[idx-length:idx]==word):
                    dp[idx] = dp[idx] or dp[idx-length]
        return dp[num_s]


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    So = Solution()
    ans = So.wordBreak(s,wordDict)
    print(ans)
