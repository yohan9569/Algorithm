# 구현 / 브론즈 1 / 단어 공부
# 단어에서 가장 많이 사용된 알파벳을 출력하는 문제

d = dict()

for a in input().upper():
    if a in d.keys():
        d[a] +=1
    else: 
      d[a]=1

m = [k for k,v in d.items() if v==max(d.values())]

if len(m)>1: 
  print('?')
else: 
  print(m[0])
