# 문자열 / 브론즈 3 / 열 개씩 끊어 출력하기

for i in range(0, len(s:=input()), 10):
    print(s[i:i+10])
