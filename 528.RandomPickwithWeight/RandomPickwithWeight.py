from typing import List
import random
import bisect
import itertools
class Solution:

    def __init__(self, w: List[int]):
        self.pre = list(itertools.accumulate(w))
        self.sum = sum(w)

    def pickIndex(self) -> int:
        x = random.randint(1, self.sum)
        # 用插入位置的概率，形成权重
        return bisect.bisect_left(self.pre, x)

if __name__ == '__main__':
    nums = [[[1, 2, 3]], [], [], []]
    actions = ["Solution","pickIndex"]
    So = Solution(nums[0][0])
    ans = So.pickIndex()
    print(ans)

