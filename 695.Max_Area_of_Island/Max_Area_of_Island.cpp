# include<vector>
# include<iostream>
# include<algorithm>
# include<string>

using namespace std;

class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int ans = 0;
        int H = grid.size(), W = H? grid[0].size() : 0, Now_Area = 0, Max_Area = 0;
        vector<vector<bool>> grid_flag(H, vector<bool>(W, false));
        for(int idx_h=0;idx_h<H;idx_h++) {
            for(int idx_w=0;idx_w<W;idx_w++) {
                if(grid_flag[idx_h][idx_w] == false && grid[idx_h][idx_w] == 1) {
                    Now_Area = FindNext(grid, grid_flag, idx_h, idx_w, H, W, Now_Area);
                    Max_Area = (Now_Area < Max_Area)? Max_Area : Now_Area;
                    Now_Area = 0;
                }
            }
        }
        ans = Max_Area;
        return ans;
    }
private:
    int FindNext(vector<vector<int>>& grid, vector<vector<bool>>& grid_flag, \
                    int idx_h, int idx_w, int H, int W, int Now_Area) {
        // 标记当前点
        grid_flag[idx_h][idx_w] = true;
        Now_Area++;
        // 寻找下个点
        if((idx_h > 0) && grid[idx_h-1][idx_w] == 1 && grid_flag[idx_h-1][idx_w] == false) {
            Now_Area = FindNext(grid, grid_flag, idx_h-1, idx_w, H, W, Now_Area);
        }
        if((idx_w > 0) && grid[idx_h][idx_w-1] == 1 && grid_flag[idx_h][idx_w-1] == false) {
            Now_Area = FindNext(grid, grid_flag, idx_h, idx_w-1, H, W, Now_Area);
        }
        if((idx_h < H-1) && grid[idx_h+1][idx_w] == 1 && grid_flag[idx_h+1][idx_w] == false) {
            Now_Area = FindNext(grid, grid_flag, idx_h+1, idx_w, H, W, Now_Area);
        }
        if((idx_w < W-1) && grid[idx_h][idx_w+1] == 1 && grid_flag[idx_h][idx_w+1] == false) {
            Now_Area = FindNext(grid, grid_flag, idx_h, idx_w+1, H, W, Now_Area);
        }
        // 找完返回
        return Now_Area;
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
