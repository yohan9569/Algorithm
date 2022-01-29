# 4344번 평균은 넘겠지

for _ in range(int(input())):
  
    l=  [int(i) for i in input().split()]
    s=l[1:]
    m=sum(s)/l[0]
    o=[i for i in s if i>m]
    
    print("{:.3f}%".format(len(o)/len(s)*100))
