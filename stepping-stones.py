# https://programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    lower = 1
    upper = 200000000
    while(lower<=upper):
        aver = (lower+upper)//2
        streak = 0
        for stone in stones:
            if stone <= aver :
                streak += 1
                if streak >= k: break
            else:
                streak = 0
        
        if streak >= k:
            upper = aver-1
        else:
            ans = aver
            lower = aver+1        
    return lower
'''
def solution(stones, k):
    last_resorts = []
    maxS = max(stones[:k])
    last_resorts.append(maxS)
    
    for idx in range(len(stones)-k):
        if stones[idx]==maxS:
            maxS = max(stones[idx+1:idx+k+1])
        else:
            maxS = max(maxS, stones[idx+k])
        if stones[idx] > maxS:
            last_resorts.append(maxS)
    
    last_resorts.sort()
    return last_resorts[0]
'''