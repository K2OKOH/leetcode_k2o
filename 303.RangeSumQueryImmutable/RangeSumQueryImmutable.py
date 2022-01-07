from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.pnums = [0]
        sum_nums = 0
        for num in nums:
            sum_nums += num
            self.pnums.append(sum_nums)
        print(self.pnums)

    def sumRange(self, left: int, right: int) -> int:
        return (self.pnums[right+1] - self.pnums[left]) 


if __name__ == '__main__':
    nums = [-2,0,3,-5,2,-1]
    So = NumArray(nums)
    left = 0
    right = 2
    ans = So.sumRange(left,right)
    print(ans)