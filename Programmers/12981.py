# Summer/Winter Coding(~2018) lv2. 영어 끝말잇기

def solution(n, words):
    ans = [0,0]
    cnt = dict()
    last = words[0][0]
    
    for i,v in enumerate(words):
        if v in cnt or v[0] != last[-1]:
            ans[1], ans[0] = divmod(i+1, n)
            
            if ans[0] == 0:
                ans[0] = n
            else:
                ans[1] += 1
            break
            
        cnt[v] = 1
        last = v

    return ans
