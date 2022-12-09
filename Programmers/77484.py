# 2021 Dev-Matching: 웹 백엔드 개발자(상반기). lv1. 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    ranking = {0:1, 1:2, 2:3, 3:4, 4:5, 5:6, 6:6}
    unknown = lottos.count(0)
    remainder = len(set(win_nums) - set(lottos))
    return [ranking[remainder-unknown], ranking[remainder]]
