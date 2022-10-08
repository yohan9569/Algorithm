# 연습문제 lv2. 피보나치 수

# first solution
def solution(n):
    fn_1 = 1
    fn_2 = 0
    fn = 0
    for _ in range(n-1):
        fn = fn_1 + fn_2
        # for next
        fn_2 = fn_1
        fn_1 = fn
    return fn%1234567


# another solution
def solution(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b,a+b# still a is a
    return b%1234567
