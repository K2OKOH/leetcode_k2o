from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n_temp = len(temperatures)
        ans = [0] * n_temp
        indices = []
        for i in range(n_temp):
            while(indices != []):
                pre_index = indices[-1]
                if (temperatures[i] <= temperatures[pre_index]):
                    break
                indices.pop()
                ans[pre_index] = i - pre_index
            indices.append(i)
        return ans



if __name__ == '__main__':
    temperatures = [73,74,75,71,69,72,76,73]
    So = Solution()
    ans = So.dailyTemperatures(temperatures)
    print(ans)
