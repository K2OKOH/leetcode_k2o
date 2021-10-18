from typing import List
import sys
import copy

class Solution:
    def backtracking(self, src: str, dst: str, wnext, wpath, ans):
        if(src == dst):
            ans.append(copy.deepcopy(wpath))
            return
        if src in wnext:
            for s in wnext[src]:
                wpath.append(s)
                self.backtracking(s, dst, wnext, wpath, ans)
                wpath.pop()

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        ans = []
        wnext = {}
        dic = []
        for w in wordList:
            dic.append(w)
        if endWord not in dic:
            return ans
        if beginWord in dic:
            dic.remove(beginWord)
        if endWord in dic:
            dic.remove(endWord)
        reversed = False
        found = False
        q1 = [beginWord]
        q2 = [endWord]
        # 队列中还有值
        while(len(q1)!=0):
            q = []
            for w in q1:
                s = w
                for i in range(len(s)):
                    ch = s[i]
                    for j in range(26):
                        letter_list = list(s)
                        letter_list[i] = chr(j + ord('a'))
                        s = ''.join(letter_list)
                        # 如果改变单词后成为终点单词
                        if(s in q2):
                            if(reversed == True):
                                if s not in wnext:
                                    wnext[s] = []
                                wnext[s].append(w)
                            else: 
                                if w not in wnext:
                                    wnext[w] = []
                                wnext[w].append(s)
                            found = True
                        # 改变后的单词，在单词列表中
                        if(s in dic):
                            if(reversed == True):
                                if s not in wnext:
                                    wnext[s] = []
                                wnext[s].append(w)
                            else:
                                if w not in wnext:
                                    wnext[w] = []
                                wnext[w].append(s)
                            q.append(s)
                    # 把字母改回来
                    letter_list = list(s)
                    letter_list[i] = ch
                    s = ''.join(letter_list)
            if(found == True):
                break
            for w in q:
                if w in dic:
                    dic.remove(w)
            if(len(q) <= len(q2)):
                q1 = q
            else:
                reversed = not reversed
                q1 = q2
                q2 = q
        if(found):
            path = [beginWord]
            self.backtracking(beginWord, endWord, wnext, path, ans)
        return ans


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    beginWord = "magic"
    endWord = "pearl"
    wordList = ["flail","halon","lexus","joint","pears","slabs","lorie","lapse","wroth","yalow","swear","cavil","piety","yogis","dhaka","laxer","tatum","provo","truss","tends","deana","dried","hutch","basho","flyby","miler","fries","floes","lingo","wider","scary","marks","perry","igloo","melts","lanny","satan","foamy","perks","denim","plugs","cloak","cyril","women","issue","rocky","marry","trash","merry","topic","hicks","dicky","prado","casio","lapel","diane","serer","paige","parry","elope","balds","dated","copra","earth","marty","slake","balms","daryl","loves","civet","sweat","daley","touch","maria","dacca","muggy","chore","felix","ogled","acids","terse","cults","darla","snubs","boats","recta","cohan","purse","joist","grosz","sheri","steam","manic","luisa","gluts","spits","boxer","abner","cooke","scowl","kenya","hasps","roger","edwin","black","terns","folks","demur","dingo","party","brian","numbs","forgo","gunny","waled","bucks","titan","ruffs","pizza","ravel","poole","suits","stoic","segre","white","lemur","belts","scums","parks","gusts","ozark","umped","heard","lorna","emile","orbit","onset","cruet","amiss","fumed","gelds","italy","rakes","loxed","kilts","mania","tombs","gaped","merge","molar","smith","tangs","misty","wefts","yawns","smile","scuff","width","paris","coded","sodom","shits","benny","pudgy","mayer","peary","curve","tulsa","ramos","thick","dogie","gourd","strop","ahmad","clove","tract","calyx","maris","wants","lipid","pearl","maybe","banjo","south","blend","diana","lanai","waged","shari","magic","duchy","decca","wried","maine","nutty","turns","satyr","holds","finks","twits","peaks","teems","peace","melon","czars","robby","tabby","shove","minty","marta","dregs","lacks","casts","aruba","stall","nurse","jewry","knuth"]
    So = Solution()
    ans = So.findLadders(beginWord, endWord, wordList)
    print(ans)
