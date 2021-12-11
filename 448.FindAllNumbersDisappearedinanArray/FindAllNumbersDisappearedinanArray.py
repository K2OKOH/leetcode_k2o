from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        n_list = [0] * n
        for i in nums:
            n_list[i-1] = 1
        for i,j in enumerate(n_list):
            if(j==0):
                ans.append(i+1)
        return ans


if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    So = Solution()
    ans = So.findDisappearedNumbers(nums)
    print(ans)