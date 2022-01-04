from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_list = {}
        longest_streak = 0
        nums_set = set(nums)
        for num in nums_set:
            # print('num:%s\tnum-1:%s' %(num,num-1))
            # 如果前面没有数字（前面有数字的话这个数就已经被统计过了）
            if (num-1 not in nums_set):
                current_num = num
                current_streak = 1
            
                while (current_num+1 in nums_set):
                    current_num += 1
                    current_streak +=1
                
                longest_streak = current_streak if (current_streak > longest_streak) else longest_streak
        
        return longest_streak



if __name__ == '__main__':
    # nums = [100,4,200,1,3,2]
    nums = [0,-1]
    So = Solution()
    ans = So.longestConsecutive(nums)
    print(ans)