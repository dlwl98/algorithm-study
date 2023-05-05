from functools import cmp_to_key

def sortBySize(a, b):
    return len(a) - len(b)

def solution(s):
    s = s[1:-1]
    result = []
    arr = []
    tmp = ''
    i = 0
    while i < len(s):
        if s[i] == '{':
            arr = []
        elif s[i] == '}':
            arr.append(int(tmp))
            tmp = ''
            result.append(arr)
        elif s[i] == ',':
            if tmp != '':
                arr.append(int(tmp))
                tmp = ''
        else:
            tmp += s[i]
        i += 1
    
    result.sort(key=cmp_to_key(sortBySize))
    
    answer = []
    for i in range(len(result)):
        tmp = result[i][0]
        answer.append(tmp)
        for j in range(i+1, len(result)):
            if tmp in result[j]:
                result[j].remove(tmp)
        
    return answer
