#https://programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    bag = dict.fromkeys(gems, 0)
    numg = len(bag.keys())
    
    minlen = len(gems)-1
    ans = [1, len(gems)]
    
    num = 0
    
    first = 0
    for i in range(len(gems)):
        last = i
        
        if not bag[gems[i]]:
            num += 1
        bag[gems[i]] += 1
        
        while (bag[gems[first]] > 1):
            bag[gems[first]] -= 1
            first += 1
        
        if num == numg:
            length = last-first
            if minlen > length:
                ans = [first+1, last+1]
                minlen = length
            
            bag[gems[first]] -= 1
            if not bag[gems[first]]:
                num -= 1
            first += 1
    
    return ans

gems = ["DIA", "RUBY", "RUBY", "RUBY", "RUBY", "RUBY", "RUBY", "RUBY", "RUBY", "RUBY", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	
#gems = ['A', 'B', 'B', 'B', 'A', 'A']
print(solution (gems))