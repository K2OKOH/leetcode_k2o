class Solution:
    
    def func2(self, nums):
        for i in range(len(nums)):
            nums[i]+=1
            
        # for num in nums:
        #     num += 1
            # print(num)
            
        return nums
    
    
    def func1(self, nums):
        
        # print(nums)
        nums_new = self.func2(nums)
        print(nums_new)
        print(nums)

def func2(nums):
    for i in range(len(nums)):
        nums[i]+=1
        
    # for num in nums:
    #     num += 1
        # print(num)
        
    return nums 
solution = Solution()

nums = [1,2,3,4]
a = func2(nums)
print(nums)