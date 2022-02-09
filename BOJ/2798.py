# 2798번. 블랙잭

n, m = map(int, input().split())
cards=[int(i) for i in input().split()]
ans=0

for i,c in enumerate(cards[:-2]):
  
    for j, d in enumerate(cards[i+1:-1]):
      
        for e in cards[i+j+2:]: # i도 더해줘야 함
            a=c+d+e
            
            if a==m: 
                ans=a
                flag=True
                break
                
            elif a<m and a>ans:
                ans=a
                
            flag=False
            
        if (flag): break
          
    if (flag): break
      
print(ans)
