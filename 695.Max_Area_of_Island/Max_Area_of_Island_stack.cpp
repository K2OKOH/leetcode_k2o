# include<vector>
# include<iostream>
# include<algorithm>
# include<string>
# include<stack>
# include<utility>

using namespace std;

class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int ans = 0;
        vector<int> dir = {-1, 0, 1, 0, -1};
        int H = grid.size(), W = H? grid[0].size() : 0, Now_Area = 0, Max_Area = 0, h, w;
        for(int idx_h=0;idx_h<H;idx_h++) {
            for(int idx_w=0;idx_w<W;idx_w++) {
                if(grid[idx_h][idx_w] == 1) {
                    Now_Area = 1;
                    grid[idx_h][idx_w] = 0;
                    // 建立stack
                    stack<pair<int, int>> island_point;
                    island_point.push({idx_h, idx_w});
                    // 开始入栈出栈
                    while(!island_point.empty()) {
                        // 出栈 并查找
                        pair<int, int> now_pos = island_point.top();
                        island_point.pop();
                        for(int k=0;k<4;k++) {
                            h = now_pos.first + dir[k];
                            w = now_pos.second + dir[k+1];
                            // 找到 并入栈
                            if(h>=0 && h<H && w>=0 && w<W && grid[h][w] == 1) {
                                grid[h][w] = 0;
                                Now_Area++;
                                island_point.push({h,w});
                            }
                        }
                    }
                    // 找完当前区域 比较大小
                    Max_Area = max(Max_Area, Now_Area);
                }
            }
        }
        ans = Max_Area;
        return ans;
    }
};
int main()
{
    Solution So;
    vector<vector<int>> grid = {{0,0,1,0,0,0,0,1,0,0,0,0,0},
                                {0,0,0,0,0,0,0,1,1,1,0,0,0},
                                {0,1,1,0,1,0,0,0,0,0,0,0,0},
                                {0,1,0,0,1,1,0,0,1,0,1,0,0},
                                {0,1,0,0,1,1,0,0,1,1,1,0,0},
                                {0,0,0,0,0,0,0,0,0,0,1,0,0},
                                {0,0,0,0,0,0,0,1,1,1,0,0,0},
                                {0,0,0,0,0,0,0,1,1,0,0,0,0}};
    int ans = 0;
    ans = So.maxAreaOfIsland(grid);
    cout << "Out: [" << ans << "]\n";
    return 0;
}
