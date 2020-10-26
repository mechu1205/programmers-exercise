#https://programmers.co.kr/learn/courses/30/lessons/60062?language=python3

import itertools

def idx_noncycadj(n, r):
    l = list(range(0,n-r+1))
    return [[idx+num for idx, num in enumerate(combo)] for combo in itertools.combinations(l, r) if not (combo[0]==0 and combo[-1]==n-r)]

def solution(n, weak, dist):
    m = len(weak)
    if m==1: return 1
    
    for r in range(1,len(dist)+1,1):
        # r: number of people
        
        if (r>=m): return m
        
        for indices in itertools.combinations(list(range (m)), r): #idx_noncycadj(m, r):
            maint_dist = [
                weak[indices[i+1]-1]-weak[indices[i]] for i in range(r-1)
            ]
            
            d = weak[indices[0]-1] - weak[indices[-1]]
            if d<0: d += n
            
            maint_dist.append(d)
            
            maint_dist.sort()
            
            isPossible = True
            for i in range(1, r+1, 1):
                if maint_dist[-i] > dist[-i]: isPossible=False
            
            if isPossible: return r
    
    return -1
