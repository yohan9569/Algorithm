# 해시 lv1. 폰켓몬

def solution(nums):
    return min(len(nums)//2, len(set(nums)))
