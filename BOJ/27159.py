# 구현 / 브론즈 3 / 노 땡스!

l=map(int,[*open(0)][1].split())
a=p=0
for i in l:
  if i>p:a+=i
  p=i+1
print(a)
