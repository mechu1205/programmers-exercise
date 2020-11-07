#https://programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque

def solution(board):
    bigboard = [None] * (2+len(board))
    for i in range(len(board)):
        bigboard [i+1] = [1] + board[i] + [1]
    bigboard[0] = [1]*(len(board[0])+2)
    bigboard[-1] = [1]*(len(board[0])+2)
    endpoint = (len(board), len(board[0]))
    
    visited = []
    q = deque([(1,1,0,0,0)]) # r, c, lastmvr, lastmvc, cost
    
    mincost = 0
    
    while len(q):
        r,c,lastmvr,lastmvc,cost = q.popleft()
        if (r,c,lastmvr,lastmvc) in visited: continue
        visited.append((r,c,lastmvr,lastmvc))
        
        for deltar,deltac in [(0,1),(0,-1),(1,0),(-1,0)]:
            if not bigboard[r+deltar][c+deltac]:
                if (deltar,deltac) == (-lastmvr,-lastmvc):
                    continue
                elif (deltar,deltac) != (lastmvr,lastmvc) and (lastmvr or lastmvc):
                    newcost = cost + 600
                else:
                    newcost = cost + 100
                
                if (r+deltar, c+deltac)==endpoint:
                    if not mincost or mincost>newcost:
                        mincost = newcost
                
                elif (r+deltar, c+deltac, deltar, deltac) not in visited:
                    found = False
                    for i, point in enumerate(q):
                        if point[-1]>=newcost:
                            q.insert(i, (r+deltar,c+deltac,deltar,deltac,newcost))
                            found = True
                            break
                    if not found:
                        q.append((r+deltar,c+deltac,deltar,deltac,newcost))
                    
    return mincost
