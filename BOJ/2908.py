# 2908번 숫자를 뒤집어서 비교
A, B = (int(''.join(list(reversed(i)))) for i in input().split())
print(max(A,B))

# 더 쉬운 # Using extended slice syntax
print(max(input()[::-1].split()))
