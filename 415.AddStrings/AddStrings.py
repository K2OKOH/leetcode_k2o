from typing import List

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        if(l1<=l2):
            num_t = num1
            num1 = num2
            num2 = num_t
            l_t = l1
            l1 = l2
            l2 = l_t

        ans = []
        step = 0
        for i in range(0,l2):
            # print(i)
            ans.append(int(num2[l2-i-1]) + int(num1[l1-i-1]) + step)
            if(ans[i] >= 10):
                ans[i] = ans[i]%10
                step = 1
            else:
                step = 0
        for j in range(l2,l1):
            # print(j)
            ans.append(int(num1[l1-j-1])+step)
            if(ans[j] >= 10):
                ans[j] = ans[j]%10
                step = 1
            else:
                step = 0
        ans = ans[::-1]
        ans = ''.join(str(i) for i in ans)
        if(step):
            ans = "1"+ans
        # print(ans)

        return ans

if __name__ == '__main__':
    num1 = "6994"
    num2 = "36"
    So = Solution()
    ans = So.addStrings(num1, num2)
    print(ans)
