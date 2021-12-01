from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        shuffled = self.nums.copy()
        n = len(shuffled)
        for i in range(n):
            j = random.randint(0,n-1)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled

if __name__ == '__main__':
    nums = [[[1, 2, 3]], [], [], []]
    actions = ["Solution", "shuffle", "reset", "shuffle"]
    So = Solution(nums[0][0])
    ans = So.shuffle()
    print(ans)
    ans = So.reset()
    print(ans)
