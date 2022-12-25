# 탐욕법(Greedy) lv2. 큰 수 만들기
# 풀이 아이디어: 가장 높은 자리부터 차례로, 선택 가능한 가장 큰 수를 남긴다.


def solution(n, k):
    ans = ''
    
    while k:
        m = '0'
        for i in range(k+1):
            m = max(m, n[i])
            if m == '9':
                break
        ans += m
        idx = n.index(m)
        n = n[idx+1:]
        k -= idx
        if k >= len(n):
            k = 0
            n = ''

    return ans + n


# better case. stack을 활용한 풀이
def solution(number, k):
    st = []
    for i in range(len(number)):
        while st and k > 0 and st[-1] < number[i]:
            st.pop()
            k -= 1
        st.append(number[i])
    return ''.join(st[:len(st) - k])
