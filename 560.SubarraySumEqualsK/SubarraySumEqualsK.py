from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        psum = 0
        hashmap = {}
        hashmap[0] = 1
        for num in nums:
            psum += num
            if ((psum-k) not in hashmap):
                hashmap[psum-k] = 0
            cnt += hashmap[psum-k]
            if (psum not in hashmap):
                hashmap[psum] = 0
            hashmap[psum] += 1
        return cnt

if __name__ == '__main__':
    nums = [1,1,1]
    k = 3
    So = Solution()
    ans = So.subarraySum(nums,k)
    print(ans)