from itertools import groupby

def dfs(arr):
    if len(arr) == 0:
        return True
    
    group = [''.join(g) for k,g in groupby(arr)]
    for i,v in enumerate(group):
        if len(v) > 1:
            group.pop(i)
            if dfs(''.join(group)):
                return True
            else:
                group.insert(i, v)
    return False
            
n = int(input())
for _ in range(n):
    s = input()
    print(1 if dfs(s) else 0)