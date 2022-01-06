from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets_map = {}
        ans = []
        s = []
        for tic in tickets:
            if (tic[0] not in tickets_map):
                tickets_map[tic[0]] = [tic[1]]
            else:
                tickets_map[tic[0]].append(tic[1])
        # print(tickets_map)
        for key in tickets_map:
            tickets_map[key].sort()
        # print(tickets_map)

        s.append('JFK')
        while(len(s) != 0):
            next_pos = s[-1]
            if (next_pos not in tickets_map):
                ans.append(next_pos)
                s.pop()
            else:
                next_p = tickets_map[next_pos].pop(0)
                s.append(next_p)
                if (tickets_map[next_pos] == []):
                    del tickets_map[next_pos]
        ans = ans[::-1]
        # print(ans)
        return(ans)

if __name__ == '__main__':
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    # tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    # tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    So = Solution()
    ans = So.findItinerary(tickets)
    print(ans)