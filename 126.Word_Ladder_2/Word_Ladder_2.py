from typing import List
import sys

class Solution:
    def backtracking(self, src: str, dst: str, wnext, wpath, ans):
        if(src == dst):
            ans.append(wpath)
            return
        for s in next[src]:
            wpath.append(s)
            self.backtracking(beginWord, endWord, wnext, wpath, ans)

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        ans = []
        wnext = {}
        if endWord not in wordList:
            return ans
        reversed = False
        found = False
        wn = len(beginWord)
        q1 = [beginWord]
        q2 = [endWord]
        # 队列中还有值
        while(len(q1)!=0):
            q = ()
            for i in range(len(q1)):
                s = q1[i]
                for i in range(len(s)):
                    ch = s[i]
                    for j in range(26):
                        s[i] = chr(j + ord('a'))
                        # 如果改变单词后成为终点单词
                        if(s in q2):
                            if(reversed == True):
                                wnext[s].append(w)
                            else:
                                wnext[w].append(s)
                            found = True
                        # 改变后的单词，在单词列表中
                        if(s in wordList):
                            if(reversed == True):
                                wnext[s].append(w)
                            else:
                                wnext[w].append(s)
                            q.append(s)
                    # 把字母改回来
                    s[i] = ch
            if(found == True):
                break
            for w in q:
                q1.remove(w)
            if(len(q1) <= len(q)):
                q1 = q1
            else:
                reversed = not reversed
                q1 = q2
                q2 = q
        if(found):
            path = [beginWord]
            self.backtracking(beginWord, endWord, next, path, ans)

        return ans


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    So = Solution()
    ans = So.findLadders(beginWord, endWord, wordList)
    print(ans)
