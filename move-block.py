#https://programmers.co.kr/learn/courses/30/lessons/60063

from collections import deque

def next(pos1, pos2, board):
    lNext = []
    
    for mv in [(1,0), (-1,0), (0,1), (0,-1)]:
        if not board[pos1[0]+mv[0]][pos1[1]+mv[1]] and not board[pos2[0]+mv[0]][pos2[1]+mv[1]]:
            lNext.append({(pos1[0]+mv[0], pos1[1]+mv[1]), (pos2[0]+mv[0], pos2[1]+mv[1])})
    
    if pos1[0]==pos2[0]:
        # I => -
        for rot in [-1,1]:
            if not board[pos1[0]+rot][pos1[1]] and not board[pos1[0]+rot][pos2[1]]:
                lNext.append({(pos1[0],pos1[1]), (pos1[0]+rot,pos1[1])})
                lNext.append({(pos1[0],pos2[1]), (pos1[0]+rot,pos2[1])})
    else:
        # - => I
        for rot in [-1,1]:
            if not board[pos1[0]][pos1[1]+rot] and not board[pos2[0]][pos2[1]+rot]:
                lNext.append({(pos1[0],pos1[1]), (pos1[0],pos1[1]+rot)})
                lNext.append({(pos2[0],pos2[1]), (pos2[0],pos2[1]+rot)})
    
    return lNext

def solution(board):
    size = len(board)
    board_pad = [None]*(size+2)
    board_pad[0] = [1]*(size+2)
    board_pad[size+1] = [1]*(size+2)
    for i in range(size):
        board_pad[i+1] = [1] + board[i] + [1]
    
    que = deque()
    visited = deque()
    
    que.append([{(1,1),(1,2)},0])
    visited.append({(1,1),(1,2)})
    
    while len(que):
        position, distance = que.popleft()
        position = list(position)
        
        for position_next in next(position[0], position[1], board_pad):
            if (size, size) in position_next: return distance+1
            if not position_next in visited:
                que.append([position_next, distance+1])
                visited.append(position_next)        
    return -1

