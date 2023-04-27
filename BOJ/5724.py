# 수학 / 브론즈 3 / 파인만

while(n:=int(input()))>0:
  a=0
  for i in range(n):a+=(n-i)**2
  print(a)


  
# another way
print(sum(i*i for i in range(n+1)))
