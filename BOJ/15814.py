# 문자열 / 브론즈 2 / 야바위 대장

i=input
s=[*i()]
for _ in range(int(i())):
    a,b=map(int,i().split())
    s[a],s[b]=s[b],s[a]
print(''.join(s))
