from operator import itemgetter

member= [(int(age), name) for age, name in (row.split() for row in [*open(0)][1:])]
for m in sorted(member, key=itemgetter(0)): print(m[0], m[1])