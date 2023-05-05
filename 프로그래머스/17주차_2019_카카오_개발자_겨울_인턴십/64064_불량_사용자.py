from itertools import permutations

def isBan(user, ban):
    if len(user) != len(ban):
        return False
    for i in range(len(user)):
        if ban[i] == '*':
            continue
        if ban[i] != user[i]:
            return False
    return True

        
def solution(user_id, banned_id):
    result = set()
    n = len(banned_id)
    for per in permutations(user_id, n):
        cnt = 0
        for i in range(n):
            if(isBan(per[i], banned_id[i])):
                cnt += 1
        if cnt == n:
            result.add(tuple(sorted(list(per))))
    
    return len(result)
