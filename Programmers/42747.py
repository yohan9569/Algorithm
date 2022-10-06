# 정렬 lv2. H-Index

def solution(citations):
    citations.sort(reverse=True)
    
    for i,v in enumerate(citations):
        if i+1 == v:
            return v
        elif i+1 > v:
            return i
    
    return len(citations)
