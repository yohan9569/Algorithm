# 연습문제 lv2. 숫자 블록
# 가장 큰 약수 구하기 == 가장 작은 약수로 나누기


def get_max_divisor(n):
    if n==1:
        return 0

    divisors=[]
    for i in range(2, int(n**0.5)+1):
        q,r = divmod(n,i)
        if not r:
            divisors.append(i)
            if q<=10**7:
                return q

    if len(divisors):
        # 약수는 있으나, 그로 나눈 몫이 전부 10^7을 넘었을 경우
        return divisors[-1]
    # 소수인 경우
    return 1


def solution(begin, end):
    ans = []
    for i in range(begin,end+1):
        a=get_max_divisor(i)
        ans.append(a)

    return ans
