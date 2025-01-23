def checkPerfect(n):
    divisors = set()
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            divisors.add(i)
            divisors.add(n//i)
    
    if sum(divisors)-n != n: return None;
    return sorted(divisors)

def printPerfect(arr):
    n = arr.pop()
    expression = " + ".join(map(str, arr))
    print(f"{n} = {expression}")

def printNot(n):
    print(f"{n} is NOT perfect.")


while(True):
    n = int(input())
    if n == -1: break
    
    arr = checkPerfect(n)
    if arr:
        printPerfect(arr)
    else:
        printNot(n)