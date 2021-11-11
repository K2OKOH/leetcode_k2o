from typing import List
import sys

class Solution:
    def convertToBase7(self, num: int) -> str:
        s = ""
        n_f = 0
        if(num==0):
            return '0'
        elif(num<0):
            n_f = 1
            num = -num
        while(num):
            s = (str(num%7)) + s
            num = num//7
        if(n_f):
            s = '-' + s
        return s

if __name__ == '__main__':
    num = -7
    So = Solution()
    ans = So.convertToBase7(num)
    print(ans)