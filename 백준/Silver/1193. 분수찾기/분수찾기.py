x=int(input())
n=0
floor=0
while x>n:
    floor+=1
    n+=floor
n-=floor
if floor%2==0:
    son=x-n
    mom=floor+1-son
else:
    mom=x-n
    son=floor+1-mom
print(f"{son}/{mom}")