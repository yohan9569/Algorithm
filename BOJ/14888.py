# 백트래킹, 브루트포스 / 실버 1 / 연산자 끼워넣기


from itertools import permutations as pm

n = int(input())
arr = [*map(int, input().split())]
a,b,c,d = map(int,input().split())
opr = a*[0]+b*[1]+c*[2]+d*[3]

oprs = set(pm(opr,n-1))

res = []
for o in oprs:
    temp = arr[0]
    for i,v in enumerate(arr[1:]):
        if o[i]==0: temp+=v
        elif o[i]==1: temp-=v
        elif o[i]==2: temp*=v
        else:
            if temp<0: temp=-(-temp//v)
            else: temp//=v
    res.append(temp)

print(max(res))
print(min(res))



# 실패 사례 # exec 함수를 이용 # 시간 초과

from itertools import permutations as pm

n=int(input())
arr=[*map(int, input().split())]
a,b,c,d=map(int,input().split())
opr=a*['+']+b*['-']+c*['*']+d*['//']

oprs=pm(opr,n-1)

res=[]
for o in oprs:
    temp=arr[0]
    for i in range(n-1):
        if temp<0 and o[i]=='//':
            temp=-(-temp//arr[i+1])
        else: exec(f'temp=temp{o[i]}arr[{i+1}]')
    res.append(temp)

print(max(res))
print(min(res))
