# boj 백준 10250번: ACM 호텔

for _ in range(int(input())):
    h,w,n = map(int,input().split())
    
    if n%h == 0: 
        ans = (h*100)+(n//h)
    else: 
        ans = (n%h*100)+(n//h+1)
        
    print(ans)
