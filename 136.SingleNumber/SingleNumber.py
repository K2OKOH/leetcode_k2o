from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans ^= n
            # print(bin(ans))
            # print('%x' %ans)
        return ans

if __name__ == '__main__':
    nums = [4,5,2,5,2]
    So = Solution()
    ans = So.singleNumber(nums)
    print(ans)
