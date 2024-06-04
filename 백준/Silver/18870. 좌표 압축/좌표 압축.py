x=[*map(int, [*open(0)][1].split())]
xs=sorted(set(x))
dic={xs[i]:i for i in range(len(xs))}
ans=[dic[j] for j in x]
print(*ans)