# 구현 / 브론즈 2 / OX퀴즈


for _ in range(int(input())):
    
    score=0
    s=0
    
    for i in input():
      
        if i=='O': 
            s+=1
            score+=s
            
        else: s=0
          
    print(score)
