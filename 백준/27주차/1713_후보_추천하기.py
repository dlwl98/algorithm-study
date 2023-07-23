from functools import cmp_to_key

n = int(input())
m = int(input())
g = list(map(int, input().split()))
isPosted = [False] * (101)
post = []

def my_cmp(a, b):
    if a[1] == b[1]:
        return b[2] - a[2]
    return b[1] - a[1]

for i in range(m):
    if (isPosted[g[i]]):
        for j in range(len(post)):
            if post[j][0] == g[i]:
                post[j][1] += 1
                post[j]
                break
    else:
        isPosted[g[i]] = True
        if len(post) >= n:
            post.sort(key=cmp_to_key(my_cmp))
            removed = post.pop()
            isPosted[removed[0]] = False
            post.append([g[i], 1, i])
        else:
            post.append([g[i], 1, i])

post.sort()
for a, b, c in post:
    print(a, end=' ')
