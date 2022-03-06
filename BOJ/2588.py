# 2588 번 곱셈

a=int(input())
b=int(input())
bstr=str(b)

print(a*int(bstr[-1]), a*int(bstr[1]), a*int(bstr[0]), a*b)
