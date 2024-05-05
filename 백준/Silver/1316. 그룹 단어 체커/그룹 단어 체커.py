N = int(input())
not_cnt = 0
for _ in range(N):
    word = list(input())
    d = dict(zip(word, [i for i in range(len(word))]))
    v = [d[k] for k in word]
    for i,n in enumerate(v[:-1]):
        if n > v[i+1]: 
            not_cnt+=1
            break
print(N-not_cnt)