# Programmers 프로그래머스 42885번 lv2 구명보트


# 작은 애부터 짝을 찾는다.
# 다음 작은 애는 그 이전 짝보다 큰 애와 짝이 될 수 없으니 range를 줄인다.


# 시간 초과 -> p1이 p2 보다 커지면 멈춘다.
def solution(people, limit):
    people.sort()
    ans=0
    idx=-1
    for i,p1 in enumerate(people):
        for p2 in people[idx:i:-1]:
            w=p1+p2
            idx-=1
            if w<=limit: 
                ans+=1
                break
    return len(people)-ans

  
# 'p1이 p2 보다 커지면 멈추고 싶은데..' -> while문으로 해결, 우수 사례 참고.
def solution(pp, lim):
    pp.sort()
    n=len(pp)
    ans=0
    i=0
    j=n-1
    while i<j:
        if pp[i]+pp[j]<=lim:
            i+=1
            ans+=1
        j-=1
    return n-ans
