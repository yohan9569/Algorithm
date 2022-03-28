# boj 백준 수학2 3009	 네 번째 점

from collections import Counter

x=[]
y=[]

for _ in range(3):
    a,b=input().split()
    x.append(a)
    y.append(b)
    
x=Counter(x)
y=Counter(y)
x=[i for i in x if x[i]==1][0]
y=[i for i in y if y[i]==1][0]

print(x,y)
