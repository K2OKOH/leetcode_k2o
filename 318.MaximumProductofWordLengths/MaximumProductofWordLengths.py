from collections import defaultdict
from typing import List
import itertools

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        ha = defaultdict(int)
        for word in words:
            mask = 0
            w_l = len(word)
            for letter in word:
                # print(letter)
                mask |= 1 << (ord(letter) - ord('a'))
                # print(mask)
            ha[mask] = max(ha[mask], w_l)
        
        for x,y in itertools.product(ha, repeat=2):
            if(x & y == 0):
                ans = max(ha[x] * ha[y], ans)

        # ans = max((ha[x] * ha[y] for x, y in itertools.product(ha, repeat=2) if x & y == 0), default=0)
        return ans


if __name__ == '__main__':
    words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    So = Solution()
    ans = So.maxProduct(words)
    print(ans)
