/*
 * @lc app=leetcode.cn id=37 lang=cpp
 *
 * [37] 解数独
 */

// @lc code=start
#include<iostream>
#include<vector>

using namespace std;
class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        // cout << "start\n";
        NextPos(board);
    }
private:
    bool judge(int i,int j,char now_num,vector<vector<char>>& board)
    {
        int area_i, area_j;
        // cout << "now_num:" << now_num << "\n";
        for(int pos=0;pos<9;pos++)  // 检查行中是否有相同元素
        {
            if(now_num==board[i][pos])
            {
                return false;
            }
        }
        for(int pos=0;pos<9;pos++)  // 检查列中是否有相同元素
        {
            if(now_num==board[pos][j])
            {
                return false;
            }
        }
        area_i = i/3;
        area_j = j/3;
        for(int pos_i=area_i*3;pos_i<area_i*3+3;pos_i++)
        {
            for(int pos_j=area_j*3;pos_j<area_j*3+3;pos_j++)
            {
                if(now_num==board[pos_i][pos_j])
                {
                    return false;
                }
            }
        }
        return true;
    }

    bool NextPos(vector<vector<char>>& board)
    {
        int i,j;
        int now_num;
        for(i=0;i<9;i++)
        {
            for(j=0;j<9;j++)
            {
                now_num = board[i][j];
                if(now_num == '.')  // 找到当前位置
                {
                    for(char test='1';test<='9';test++)   // 尝试9个数
                    {
                        if(judge(i,j,test,board) == true)
                        {
                            board[i][j] = test;
                            if(NextPos(board) == true)
                                return true;
                            board[i][j] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
};
// @lc code=end

