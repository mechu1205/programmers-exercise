# https://programmers.co.kr/learn/courses/30/lessons/64064
from itertools import combinations

def match(string, pattern):
    length = len(string)
    if (len(pattern)!=length): return False
    for i in range(length):
        if pattern[i] != string[i] and pattern[i] != '*': return False
    return True

def targets(z, taken):
    if not len(z): return [taken]
    num, cands = z[0]
    cands = [cand for cand in cands if cand not in taken]
    if len(cands)<num: return []
    
    ans = []
    for combo in combinations(cands, num):
        ans += targets(z[1:], taken+list(combo))
    
    return ans

def solution(user_id, banned_id):
    bans = dict()
    map = dict()
    
    for id in banned_id:
        if id in bans:
            bans[id] +=1
        else:
            bans[id] = 1
    
    for ban in bans:
        map[ban] = []
        for idx, user in enumerate(user_id):
            if match(user, ban): map[ban].append(idx)
    
    z = list(zip(bans.values(), map.values()))

    combos = targets(z, [])
    
    combos = [combo for combo in combos if len(combo)==len(banned_id)]
    combos = list(set([''.join([str(idx) for idx in sorted(combo)]) for combo in combos]))
    return len(combos)
        

print(solution (["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution (["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution (["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))