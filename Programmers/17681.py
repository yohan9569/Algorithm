# 2018 KAKAO BLIND RECRUITMENT lv1. [1차] 비밀지도

def solution(n, arr1, arr2):
    bin1 = [bin(i)[2:] for i in arr1]
    bin2 = [bin(i)[2:] for i in arr2]
    
    ans = []
    for a,b in zip(bin1,bin2):
        a = (n-len(a))*"0" + a
        b = (n-len(b))*"0" + b
        
        tmp = ""
        for c,d in zip(a,b):
            if int(c)+int(d):
                tmp += "#"
            else:
                tmp += " "
        ans.append(tmp)
        
    return ans
