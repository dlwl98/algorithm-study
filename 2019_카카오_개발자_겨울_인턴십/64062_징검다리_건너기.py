def solution(stones, k):
    def go(degree):
        x = 0
        y = 0
        for stone in stones:
            y += 1
            if stone - degree > 0:
                if x+k < y: return False
                x = y
        y += 1
        if x+k < y: return False
        return True
    
    s = 0
    e = 200000001
    while s < e:
        mid = (s + e) // 2
        if go(mid):
            s = mid + 1
        else:
            e = mid
        
    return s
