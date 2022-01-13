class Solution:
    def calculate(self, s: str) -> int:
        idx = 0
        return self.Expr(s, idx)

    def Expr(self, s: str, idx: int) -> int:
        op = '+'
        l_n = 0
        r_n = 0
        while(idx < len(s)):
            if (s[idx] != ' '):
                n = self.FindNum(s, idx)
                # 如果是加减法（低优先级），先完成上一次的运算
                # 再把本次的（值，符号）放入 right number
                if (op == '+'):
                    # 完成上一次的运算
                    l_n += r_n
                    # 赋予这次的新的值
                    r_n = n
                elif (op == '-'):
                    l_n += r_n
                    r_n = -n
                # 如果是乘除法（高优先级），直接在右边值上操作
                elif (op == '*'):
                    r_n *= n
                elif (op == '/'):
                    r_n = int(r_n/n)
                # 找到运算符
                if (idx < len(s)):
                    op = s[idx]
            idx += 1
        return l_n + r_n

    # 从当前位置 i 找一个完整的数字
    def FindNum(self, s: str, idx: int) -> int:
        n = 0
        # 找到运算符后停止
        while(idx<len(s) and s[idx].isdigit()):
            n = 10*n + int(s[idx])
            idx += 1
        return n


if __name__ == '__main__':
    s = " 3/2 "
    So = Solution()
    ans = So.calculate(s)
    print(ans)