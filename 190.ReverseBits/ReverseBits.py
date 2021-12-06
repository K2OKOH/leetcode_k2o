from typing import List

class Solution:
    def reverseBits(self, n: int) -> int:
        # print("%x" %n)
        ans = 0
        for i in range(32):
            # print('i:%d' %i)
            if(i<16):
                ans |= (n & 0x0001<<i) << (31-i*2)
            else:
                ans |= (n & 0x0001<<i) >> ((i-15)*2-1)
            # print('ans:%x' %ans)
        return ans

if __name__ == '__main__':
    n = 0b00000010100101000001111010011100
    So = Solution()
    ans = So.reverseBits(n)
    print(ans)
