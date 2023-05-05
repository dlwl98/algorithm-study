import sys
sys.setrecursionlimit(10**6)

def solution(k, room_number):
    parent = {}
    result = []
    
    def find(i):
        if i not in parent:
            parent[i] = i
            return i
        if parent[i] == i:
            return i;
        parent[i] = find(parent[i])
        return parent[i]
    
    for num in room_number:
        x = find(num)
        result.append(x)
        y = find(x+1)
        parent[x] = y
            
    return result
