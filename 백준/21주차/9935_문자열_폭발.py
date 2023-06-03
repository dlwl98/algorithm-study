a = input()
boom = input()
s = []

def check():
    if ''.join(s[-len(boom):]) == boom:
        return True
    return False

for x in a:
    s.append(x)
    if len(s) < len(boom):
        continue
    while check():
        for _ in range(len(boom)):
            s.pop()

print("FRULA" if ''.join(s) == '' else ''.join(s))
