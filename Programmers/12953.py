# 연습문제 lv2. N개의 최소공배수

def solution(arr):
    # import math
    # return math.lcm(arr)  # New in version 3.9.
    
    mx = max(arr)
    lcd = 0
    arr2 = []
    while len(arr) != len(arr2):
        lcd += mx
        arr2 = [i for i in arr if lcd%i == 0]
    
    return lcd
