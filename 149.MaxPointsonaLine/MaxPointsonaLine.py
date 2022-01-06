from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        same_y = 1
        same = 1
        max_cnt = 0
        n_points = len(points)
        for dot1 in range(n_points):
            hash_list = {}
            same_y = 1
            same = 1
            for dot2 in range(dot1+1, n_points):
                # 如果x方向值相同 (斜率不存在)
                if (points[dot1][0] == points[dot2][0]):
                    same_y += 1
                    # 如果两个是同一个点
                    if (points[dot1][1] == points[dot2][1]):
                        same += 1
                # 斜率存在
                else: 
                    slope = (points[dot1][1] - points[dot2][1]) / (points[dot1][0] - points[dot2][0])
                    if (slope not in hash_list):
                        hash_list[slope] = 1
                    else:
                        hash_list[slope] += 1


            max_cnt = same_y if (same_y > max_cnt) else max_cnt
            
            for key in hash_list:
                max_cnt = max(max_cnt, same + hash_list[key])

        return max_cnt

if __name__ == '__main__':
    Input = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    So = Solution()
    ans = So.maxPoints(Input)
    print(ans)