# programmers 프로그래머스 42748번 K번째수 Lv.1

def solution(array, commands):
    ans=[]
    for c in commands:
        arr=array[c[0]-1 : c[1]]
        ans.append(sorted(arr)[c[2]-1])
    return ans
