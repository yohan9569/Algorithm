# 1316번. 그룹 단어 체커.

# 단어의 알파벳 리스트[h,a,p,p,y,a]를 원래 순서대로 딕셔너리로 만든다.
# 밸류로 리스트를 만든다 [0,1,2,2,3,1]
# 다음 인자보다 이전 인자가 크면 그룹 단어가 아니다.
# -> 바뀜: 알파벳마다 마지막 나온 인덱스로 매핑됨. [0,5,3,3,4,5]

N = int(input())
not_cnt = 0
for _ in range(N):
    word = list(input())
    d = dict(zip(word, [i for i in range(len(word))]))
    v = [d[k] for k in word]
    for i,n in enumerate(v[:-1]):
        if n > v[i+1]: 
            not_cnt+=1
            break
print(N-not_cnt)

# 숏코딩: print(sum([*x]==sorted(x,key=x.find)for x in open(0))-1)
