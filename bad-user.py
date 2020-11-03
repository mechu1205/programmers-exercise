# https://programmers.co.kr/learn/courses/30/lessons/64064

def match(string, pattern):
    length = len(string)
    if (len(pattern)!=length): return False
    for i in range(length):
        if pattern[i] != string[i] and pattern[i] != '*': return False
    return True


def solution(user_id, banned_id):
    answer = 0
    return answer
    
    bans = dict()
    #lCands = list()
    map = dict()
    
    for id in banned_id:
        if id in bans:
            bans[id] +=1
        else:
            bans[id] = 1
    '''
    for ban in bans:
        lCands.append([])
        for idx, user in enumerate(user_id):
            if match(user, ban): lCands[-1].append(idx)    
        '''
    
    for ban in bans:
        map[ban] = []
        for idx, user in enumerate(user_id):
            if match(user, ban): map[ban].append(idx)
        
    for lCand in lCands[temp]:
'''
strat
map bannedid to userid
for bannedid in unique(banned_id):
    for all possible combination of matches for all occurrences of bannedid,
    do recursion
'''