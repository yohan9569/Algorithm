# 구현, 문자열 / 브론즈 2 / 팰린드롬인지 확인하기


l = len(s:=input())//2
if s[:l] == s[:-l-1:-1]:
    a = 1
else:
    a = 0
print(a)


# another way
s=input();print(+(s==s[::-1])) # +True == 1
