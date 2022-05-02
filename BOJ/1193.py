# boj 백준 수학 1193번 분수찾기

x = int(input())
n = 0 # 층을 시작하는 순서
floor = 0 # 몇 층인지 == 그 층에 몇 개가 있는지

while x>n:
    floor += 1
    n += floor
    
n -= floor # 다음 층 시작하는 순서이므로 한 층 빼 줌

if floor%2==0:
    son = x-n
    mom = floor+1-son
else:
    mom = x-n
    son = floor+1-mom
    
print(f"{son}/{mom}")
