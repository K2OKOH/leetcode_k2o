from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        hash_list = {}
        for idx in range(len(nums)):
            if ((target - nums[idx]) in hash_list):
                ans.append(hash_list[target - nums[idx]])
                ans.append(idx)
            else:
                hash_list[nums[idx]] = idx
        return ans


if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    So = Solution()
    ans = So.twoSum(nums, target)
    print(ans)