# include<vector>
# include<iostream>
# include<algorithm>
# include<string>

using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int W = board[0].size(), H = board.size();
        vector<vector<bool>> visited(H, vector<bool>(W,false));
        bool ans = false;
        int cnt = 0;
        for(int idx_y=0;idx_y<H;idx_y++) {
            for(int idx_x=0;idx_x<W;idx_x++) {
                backtracking(idx_x, idx_y, board, word, visited, 0, ans);
            }
        }
        return ans;
    }
private:
    void backtracking(int x, int y, vector<vector<char>>& board, \
                        string word, vector<vector<bool>>& visited, int cnt, bool & ans) {
        // 跳过条件
        if (x<0 || y<0 || x>=board[0].size() || y>=board.size() || \
            visited[y][x] == true || ans == true || board[y][x] != word[cnt]) {
            return;
        }
        // 找到条件
        if(cnt == word.size() - 1) {
            ans = true;
            return;
        }
        // 找下一个
        visited[y][x] = true;
        backtracking(x+1, y, board, word, visited, cnt+1, ans);
        backtracking(x-1, y, board, word, visited, cnt+1, ans);
        backtracking(x, y+1, board, word, visited, cnt+1, ans);
        backtracking(x, y-1, board, word, visited, cnt+1, ans);
        visited[y][x] = false;
    }
};

int main()
{
    Solution So;
    string word = "ABCB";
    bool ans = false;
    vector<vector<char>> board = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
    ans = So.exist(board, word);
    cout << ans << endl;
    return 0;
}
