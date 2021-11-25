from typing import List
import sys

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        way = []
        for idx in range(len(expression)):
            c = expression[idx]
            if(c=='+' or c=='-' or c=='*'):
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx+1:])
                for l in left:
                    for r in right:
                        if(c == '+'):
                            way.append(l+r)
                        elif(c == '-'):
                            way.append(l-r)
                        elif(c == '*'):
                            way.append(l*r)
        if(len(way)==0):
            way.append(int(expression))
        return way

if __name__ == '__main__':
    expression = "2*3-4*5"
    So = Solution()
    ans = So.diffWaysToCompute(expression)
    print(ans)
