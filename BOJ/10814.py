# 정렬 / 실버 5 / 나이순 정렬

from operator import itemgetter

member = [(int(age), name) for age, name in (row.split() for row in [*open(0)][1:]) ]

for m in sorted(member, key=itemgetter(0)): 
    print(m[0], m[1])


# another way
print(*sorted([*open(0)][1:],key=lambda a:int(a.split()[0])),sep='')
