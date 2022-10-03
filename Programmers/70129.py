# 월간 코드 챌린지 시즌1 - 이진 변환 반복하기


def izin(s, cnt, zero):
    new = s.replace("0", "")
    cnt += 1
    zero += (len(s) - len(new))
    new  = str(bin(len(new))[2:])
    
    if new == "1":
        return new, cnt, zero
    else:
        return izin(new, cnt, zero)

def solution(s):
    _, a, b = izin(s, 0, 0)
    return [a,b]
