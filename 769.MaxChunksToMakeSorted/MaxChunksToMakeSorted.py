from typing import List, Text

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        n_max = 0
        for i in range(n):
            n_max = max(n_max, arr[i])
            if(n_max == i):
                ans += 1
        return ans

if __name__ == '__main__':
    arr = [1,0,2,3,4]
    So = Solution()
    ans = So.maxChunksToSorted(arr)
    print(ans)